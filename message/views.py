from django.shortcuts import render, redirect, get_object_or_404  
from .models import Message
from checkmateapp.models import Mate
from account.models import CustomUser
from .forms import MessageForm
from django.utils import timezone

def receive_box(request):
    messages = Message.objects.filter(receiver = request.user)
    return render(request, "receive_box.html", {'messages':messages})

def send_box(request):
    messages = Message.objects.filter(sender = request.user) 
    return render(request, "send_box.html", {'messages':messages})

def detail_message(request, id):
    message = get_object_or_404(Message, pk = id)
    return render(request, 'detail_message.html', {'message':message})

def new_message(request, post_id):
    if request.method == 'POST':
        message_form = MessageForm(request.POST)
        if message_form.is_valid():
            new_message = message_form.save(commit=False)  # 임시저장
            new_message.sender = request.user
            new_message.receiver = get_object_or_404(Mate, pk=post_id).writer
            new_message.send_date = timezone.now()
            new_message.save()
            return redirect('message:send_box')
    else:
        message_form = MessageForm()
        return render(request, 'new_message.html', {'message_form':message_form})

