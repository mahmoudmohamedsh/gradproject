from django.shortcuts import render
from .serializers import StudentUserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets,filters,generics,permissions
# Create your views here.

class CreateUser(APIView):
    # permission_class = [permissions.IsAdmin]

    def post(self, request , format = None):
        print(request.data)
        serializer = StudentUserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST) # bad request

        serializer.save()
        return Response(serializer.data , status=status.HTTP_200_OK) # ok

    def get(self,request):
        print('here')
        return Response("done", status=status.HTTP_200_OK) # ok
