from django.db import models
from django.conf import settings 
from checkmateapp.models import Mate

class Message(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sender')  # 쪽지 보내는 사람
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='receiver')  # 쪽지 받는 사람
    send_date = models.DateTimeField()
    content = models.TextField()

    def summary(self):
        return self.content[:50]  