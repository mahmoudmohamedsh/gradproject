from django.db import models
from django.utils import timezone
# Create your models here.
def uploat_to(instance , filename):
    return 'post/{filename}'.format(filename=str(instance.created_at)+" "+filename)


class Announcement(models.Model):
     
    title = models.CharField(max_length=255,default="")
    img = models.ImageField(null = True , blank = True,upload_to = uploat_to, default='')
    created_at = models.DateTimeField(default=timezone.now)
    # created_at = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self) :
        return str(self.created_at)