from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    mbti_Choices = (
        ('모름','모름'),
        ('ISTJ','ISTJ'),
        ('ISFJ','ISFJ'),
        ('INFJ','INFJ'),
        ('INTJ','INTJ'),
        ('ISTP','ISTP'),
        ('ISFP','ISFP'),
        ('INTP','INTP'),
        ('INFP','INFP'),
        ('ESTP','ESTP'),
        ('ESFP','ESFP'),
        ('ENFP','ENFP'),
        ('ENTP','ENTP'),
        ('ESTJ','ESTJ'),
        ('ESFJ','ESFJ'),
        ('ENFJ','ENFJ'),
        ('ENTJ','ENTJ'),
    )
    mbti = models.TextField(choices=mbti_Choices)
    location = models.CharField(max_length=200)