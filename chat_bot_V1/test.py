## file content :
#================
##  makeChatTrain()
##  model,words,labels = makeModel()
##  bag_of_words()
##  chat()
##  predict_chat()


from statistics import mode
import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

import numpy
import tflearn
import tensorflow.compat.v1 as tf
import random
import json
import pickle
import os






pathtochat = os.path.join(os.getcwd(),'chat_bot_V1') 
print("===========",pathtochat)

'''
delete all files save to force chat to create it 
'''
def makeChatTrain():
    dir = pathtochat+'model'
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))
    dir = pathtochat+'data'
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))


intents_file_path = os.path.join(pathtochat,"intents.json")


with open(intents_file_path) as file:
    data = json.load(file)

'''
make train data and make model and train it 
'''
def makeModel():
    try:
        with open(pathtochat+"/data/data.pickle", "rb") as f:
            words, labels, training, output = pickle.load(f)
    except:
        words = []
        labels = []
        docs_x = []
        docs_y = []

        for intent in data["intents"]:
            for pattern in intent["patterns"]:
                wrds = nltk.word_tokenize(pattern)
                words.extend(wrds)
                docs_x.append(wrds)
                docs_y.append(intent["tag"])

            if intent["tag"] not in labels:
                labels.append(intent["tag"])

        words = [stemmer.stem(w.lower()) for w in words if w != "?"]
        words = sorted(list(set(words)))

        labels = sorted(labels)

        training = []
        output = []

        out_empty = [0 for _ in range(len(labels))]

        for x, doc in enumerate(docs_x):
            bag = []

            wrds = [stemmer.stem(w.lower()) for w in doc]

            for w in words:
                if w in wrds:
                    bag.append(1)
                else:
                    bag.append(0)

            output_row = out_empty[:]
            output_row[labels.index(docs_y[x])] = 1

            training.append(bag)     # [[0,0,....,0],[0,0,....,0],[0,0,....,0]]
            output.append(output_row)# [[0,0,0,0,1],[0,0,....,0],[0,0,....,0]]


        training = numpy.array(training)
        output = numpy.array(output)

        with open(pathtochat+"/data/data.pickle", "wb") as f:
            pickle.dump((words, labels, training, output), f)
    '''
    tensorflow.reset_default_graph()
    This function is deprecated. Use tf.compat.v1.reset_default_graph() instead.
    '''
    tf.reset_default_graph()

    net = tflearn.input_data(shape=[None, len(training[0])],name='input')
    net = tflearn.fully_connected(net, 8)
    net = tflearn.fully_connected(net, 8)
    net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
    net = tflearn.regression(net)

    model = tflearn.DNN(net)
    #-------------------------------------------------------------------------------
    # old code with some test to check 
    #==================================
    # try:
    #     model.load("model.tflearn")
    # except:
    #     print("--------------------------")
    #     print(training[0].shape)#26x46
    #     print("--------------------------")
    #     print(output.shape)#26x6
    #     print("--------------------------")
    #     # model.fit(training, output, n_epoch=1000, batch_size=8, show_metric=True)
    #     model = tflearn.DNN(net)
    #     model.fit(training,output)
    #     model.save("model.tflearn")
    #-------------------------------------------------------------------------------
    if os.path.exists(pathtochat+"/model/model.tflearn.meta"):
        model.load(pathtochat+"/model/model.tflearn")
    else:
        model.fit(training, output, n_epoch=1000, batch_size=8, show_metric=True)
        model.save(pathtochat+"/model/model.tflearn")   
    return model,words,labels

'''
convert lines that user enter to bag of words or you can call it one hot incoded
'''
def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1
            
    return numpy.array(bag)

model,words,labels = makeModel()

'''
predict function
'''
def predict_chat(inp):
    results = model.predict([bag_of_words(inp, words)])
    results_index = numpy.argmax(results)
    tag = labels[results_index]

    for tg in data["intents"]:
        if tg['tag'] == tag:
            responses = tg['responses']
    message =random.choice(responses)
    print("==========",message)
    return message
'''
start chat with the bot in terminal for test with no neet to api requests
'''
def chat():
    print("Start talking with the bot (type quit to stop)!")
    while True:
        inp = input("You: ")
        if inp.lower() == "quit":
            break

        results = model.predict([bag_of_words(inp, words)])
        results_index = numpy.argmax(results)
        tag = labels[results_index]

        for tg in data["intents"]:
            if tg['tag'] == tag:
                responses = tg['responses']
        message = random.choice(responses)
        print(message)
        return message

#
# get the model and date to start predict
#
# test
# makeChatTrain()
# model,words,labels = makeModel()
# chat()