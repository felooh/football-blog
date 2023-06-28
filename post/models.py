from django.db import models
import os


# Create your models here.

def get_upload_path(instance, filename):
    return os.path.join("images","post_image", str(instance.pk), filename)

class Post(models.Model):
    category = models.CharField(max_length=15)
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=1023)
    image = models.ImageField(upload_to=get_upload_path, blank=True, null=True)    
    author_name = models.CharField(max_length=15)


