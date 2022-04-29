GET /home/
no data send
res 
[
    {
        "title": "hello post",
        "img": "/media/post/None_92b7ebd50132ac26f4d91d99988260c0998dffaa2fac56728fd8ddb9de5d92b6_9UvyHmO.jpg",
        "created_at": "2022-04-29T02:49:54.138502Z"
    },
    {
        "title": "hello post",
        "img": "/media/post/None_92b7ebd50132ac26f4d91d99988260c0998dffaa2fac56728fd8ddb9de5d92b6_gRmmEIs.jpg",
        "created_at": "2022-04-29T02:49:09.355569Z"
    },
    ......
]
==================================
POST /home/
if user is admin will allow him to add post
send
{'title':"" , "img":"" }


=================================
GET /home/chat 
send
? message = value
    res {"message" : " "}
if no value you will get 
    res {"error" : " "}

=================================
Post /home/mail
send
{
'from':"",
'subject':"",
'body':""
}
res {'done' : True}
=================================