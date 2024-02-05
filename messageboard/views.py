from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from . import models
from .models import Message


# Create your views here.

def index(request):

    message = Message.objects.all()
    return render(request, 'messageboard/index.html', {
        "message" : message,
    })

def create(request):
    
    if request.method == "POST":
            user = request.POST.get("user")
            title = request.POST.get("title")
            content = request.POST.get("content")
            message = models.Message(title=title, content=content, user=user)
            message.save()
    
    #return HttpResponseRedirect(reverse('create'))
    return render(request, 'messageboard/create.html')



def edit(request):
    
    return render(request, 'messageboard/edit.html')


def register(request):
    
    return render(request, 'messageboard/register.html')