from django import forms
from .models import Message

class MessageForm(forms.ModelForm): # 장고에서 지원해주는 forms를 상솓받음
    class Meta: 
        model = Message
        fields = ['content']