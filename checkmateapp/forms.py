from django import forms
from .models import Mate, Comment

class mateForm(forms.ModelForm):
    class Meta:
        model = Mate
        fields = ['title', 'mate_type', 'activity_area', 'people_number', 'explanation', 'img']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']