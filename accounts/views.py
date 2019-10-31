from django.shortcuts import render,redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is being used')
                else:
                    user = User.objects.create_user(username=username, password=password, email=email,first_name=first_name, last_name=last_name)
                    user.save()
                    messages.success(request, 'You are now registered and can login')
                    return redirect('login')


        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in!')
            return redirect('userprofile')
        else:
            messages.error(request, 'Wrong credentials')
            return redirect('login')

    else:
        return render(request, 'accounts/login.html')
@login_required(login_url='/accounts/signup')
def userprofile(request):
#    profile = request.user.get_profile()
    return render(request, 'accounts/userprofile.html')


