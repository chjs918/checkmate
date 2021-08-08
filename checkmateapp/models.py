from django.db import models
from django.db.models.fields.related import ForeignKey
from account.models import CustomUser
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.
class Mate(models.Model):
    title = models.CharField(max_length=50)
    mate_type = models.CharField(max_length=50)
    writer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='usernames')
    activity_area = models.CharField(max_length=50)
    explanation = models.TextField()
    people_number = models.CharField(max_length=50)
    img = models.ImageField(upload_to="mate/", blank = True, null = True)
    image_thumbnail = ImageSpecField(source = 'img', processors=[ResizeToFill(120,100)])

    def __str__(self):
        return self.title
 