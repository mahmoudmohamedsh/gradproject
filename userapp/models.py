#my import
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
# Create your models here.  |
#---------------------------|
#   student model , manager |
#   
# 
#  #

# https://www.youtube.com/watch?v=V2zaeqFSSTE
# save the img functions
def uploat_to(instance , filename):
    return 'users/{filename}'.format(filename=instance.username+" "+filename+".png")


class StudentUserManager(BaseUserManager):

    def create_user(self,code,username,password,**other_fields):
        if not code :
            raise ValueError('you must enter code')

        user = self.model(code=code ,username=username ,**other_fields )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,code,username,password,**other_fields):
        other_fields.setdefault('is_staff',True)
        other_fields.setdefault('is_superuser',True)

        if other_fields.get("is_staff") is not True:
            raise ValueError('superuser must be staff')

        if other_fields.get("is_superuser") is not True:
            raise ValueError('superuser must be superuser')

        user = self.create_user(code,username,password,**other_fields)
        
        return user


# basic inf for student that is required for each student
# { code 'pk', username ,gpa ,img ,level , hour , is_staff, created_at , updated_at}
class StudentUser(AbstractBaseUser,PermissionsMixin):
    LEVEL_OPTIONS = (
        ('lvl 1', 'level one'),
        ('lvl 2', 'level two'),
        ('lvl 3', 'level three'),
        ('lvl 4', 'level four'),
        
    )
    code = models.CharField(max_length=255,unique=True)
    username = models.CharField(max_length=255)
    gpa = models.FloatField(max_length=5,default=0)
    img = models.ImageField(null = True , blank = True,upload_to = uploat_to, default='')
    level = models.CharField(choices=LEVEL_OPTIONS,max_length=64,default=LEVEL_OPTIONS[0])
    hour = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'code'
    REQUIRED_FIELDS = ['username']

    object = StudentUserManager()
    def __str__(self) :
        return self.code +" - "+ self.username

# in setting add this
#   AUTH_USER_MODEL = link to this model
#   AUTH_USER_MODEL = 'userapp.StudentUser'

# in admin.py
#   import the model
#   admin.site.register(model)

