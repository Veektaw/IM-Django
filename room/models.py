from django.db import models
from chat.models import *
# Create your models here.
class Room(models.Model):
    name = models.CharField (max_length=255)
    slug = models.SlugField (unique=True)
    
class Message (models .Model):
    room = models. ForeignKey (Room, related_name= 'messages', on_delete=models.CASCADE)
    user = models. ForeignKey (User, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models. DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('created_at',)