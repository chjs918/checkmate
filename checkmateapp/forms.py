from django import forms
from .models import Mate

class mateForm(forms.ModelForm):
    class Meta:
        model = Mate
        fields = ['title', 'mate_type', 'activity_area', 'people_number', 'explanation', 'img']