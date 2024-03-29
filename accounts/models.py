from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    about = models.TextField(max_length=255,default='Im user of cool site with cool features')
