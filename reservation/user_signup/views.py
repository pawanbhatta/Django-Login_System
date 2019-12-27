from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.


def signup(request):

    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        re_password = request.POST['re_password']

        if password == re_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, "User Already Exists")
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already in use')
                return redirect('signup')
            else:
                user = User.objects.create_user(
                    username=username, first_name=first_name, last_name=last_name, email=email, password=password)
                user.save()
                print("User Created")

                return redirect('login')

        else:
            messages.info(request, 'Password did not match')
            return redirect('signup')

        return redirect('/')

    else:
        return render(request, 'signup/signup.html')
