from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Use(models.Model): 
    name = models.CharField(max_length=50) 
    x_ray_img = models.ImageField(upload_to='images/') 
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)