from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime
from django.db.models.signals import post_save
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver


User = get_user_model()

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.user.get_username()
    


# class Conversation(models.Model):
#     conversation_id = models.AutoField(primary_key=True)  
#     participants = models.ManyToManyField(User, related_name='conversations')
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Conversation {self.conversation_id}"
    
    
# class Message(models.Model):
#     conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
#     sender = models.ForeignKey(User, on_delete=models.CASCADE)
#     content = models.TextField()
#     timestamp = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         ordering = ['timestamp']



