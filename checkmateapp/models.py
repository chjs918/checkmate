from django.db import models
from django.db.models.fields.related import ForeignKey
from django.conf import settings 
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.
class Mate(models.Model):
    title = models.CharField(max_length=50)
    mate_type_Choices = (
        ('문화생활 메이트','문화생활 메이트'),
        ('국내•해외여행 메이트','국내•해외여행 메이트'),
        ('캠핑 메이트','캠핑 메이트'),
        ('운동 메이트','운동 메이트'),
        ('공부 메이트','공부 메이트'),
    )
    mate_type = models.TextField(choices=mate_type_Choices)
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    activity_area = models.CharField(max_length=50)
    explanation = models.TextField()
    people_number = models.CharField(max_length=50)
    created_at = models.DateTimeField()

    img = models.ImageField(upload_to="mate/", blank = True, null = True)
    image_thumbnail = ImageSpecField(source = 'img', processors=[ResizeToFill(120,100)])

    def __str__(self):
        return self.title

class Comment(models.Model):
    post_id = models.ForeignKey("Mate", on_delete=models.CASCADE, db_column="post_id")
    comment_id = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    body = models.TextField()