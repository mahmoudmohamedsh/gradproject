from rest_framework import serializers
from .models import StudentUser
from django.conf import settings


class StudentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentUser
        fields = ('code',"username",'gpa','img','level','hour')
        extra_kwergs = {'password': {'write_only':True }}



