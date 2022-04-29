from ast import Pass
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status , permissions
from .models import Announcement
from .serializers import AnnouncementSerializer
from rest_framework.decorators import api_view
from django.conf import settings
import os
# rotate to the chat bot file to import the files
pathtochat = os.path.join(settings.BASE_DIR,'chat_bot_V1') 
import sys
sys.path.insert(1, pathtochat)
import test # class contain all require methods to create model , make predections of questions


# Create your views here. that handle requests

###
# class for handle the list of announcement and the add announcement requests
# url => /home/
class HomeList(APIView):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self,request ,formate=None):
        announcement = Announcement.objects.all().order_by('-created_at')
        serialized_date = AnnouncementSerializer(announcement,many=True)

        return Response(serialized_date.data,status=status.HTTP_200_OK)

    def post(self,request,formate=None):
        serialize = AnnouncementSerializer(data=request.data)
        if serialize.is_valid() :
            serialize.save()
            return Response(serialize.data, status=status.HTTP_201_CREATED)
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)

###
# take user question and return the bot answer  
# url => /home/chat
@api_view(['GET'])
def api_chatbot(req,*arg,**kwargs):
    # res = test.predict_chat(req.data['message']) # for post request
    if(not req.GET.get("message")):
        return Response({"error":"missing the message"} , status=status.HTTP_400_BAD_REQUEST)
    res = test.predict_chat(req.GET.get("message"))
    return Response({"message":res} , status=status.HTTP_200_OK)

###
# send email from user to us with his email , title and email body 
# url => /home/mail
from django.core.mail import EmailMessage , send_mail
from django.template.loader import render_to_string
@api_view(['POST'])
def api_send_mail(req,*arg,**kwargs):
    emailfrom = req.data['from']
    name = req.data['name']
    subject =  req.data['subject']
    body = req.data['body']

    TEMPLATE_DIRS = os.path.join(settings.BASE_DIR,'public' ,'emailtemp.html'),
    
    temp = 'name: {name} , email :{emailfrom}, subject:{subject} , body : {body}'.format(
        name=name,emailfrom= emailfrom, subject=subject, body=body
    )

    email = EmailMessage(
        subject = subject,
        body = temp,
        #sending email
        from_email = settings.EMAIL_HOST_USER,
        #list of empolyee send to
        to=['201727100@std.sci.cu.edu.eg'],

    )
    email.fail_silently = False
    email.send()
    # send_mail('hello','hello there my name is sharp'
    # ,'test@test.com',['201727100@std.sci.cu.edu.eg'],fail_silently=False)
    return Response({'done' : True}, status=status.HTTP_200_OK)


    




