from django.shortcuts import render
from .models import App

def resize_picture(request):
    content = App.objects.all()
    return render(request, 'resize_picture.html', {'content': content})
