from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.


def index(request):
    return render(request, 'index.html')


def logout(request):
    auth.logout(request)
    return redirect('index')


def mail(request):
    if request.method == 'POST':
        username = request.POST['username']
        message = request.POST['message']
        send_mail(username, message, settings.EMAIL_HOST_USER, [
                  request.POST['email']], fail_silently=False)
        return redirect('/')

    else:
        return redirect('/')
