from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Room(models.Model):
   name = models.CharField(max_length = 100)
   def __str__(self):
      return self.name
   

class Message(models.Model):
   message = models.CharField(max_length = 10000)
   date = models.DateField(default = timezone.now())
   time = models.TimeField(default = timezone.now())
   timestamp = models.DateTimeField(auto_now_add=True)
   room = models.ForeignKey(Room , on_delete=models.CASCADE)
   user = models.ForeignKey(User , on_delete=models.CASCADE)
   username = models.CharField(max_length = 500 , default = '')
