from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.db import IntegrityError
def register(request):
    if request.method == 'POST':
        #first_name = request.POST['first_name']
        #last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Это имя занято')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Эта почта уже используется')
                else:
                    about = 'Im a user of this cool forum'
                    user = User.objects.create_user(username=username, password=password, email=email,first_name=first_name, last_name=last_name)
                    user.save()
                    messages.success(request, 'Вы успешно зарегистрировались и можете войти')
                    return redirect('login')


        else:
            messages.error(request, 'Пароли не совпадают')
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
            messages.success(request, 'Вы вошли!')
            return redirect('userprofile')
        else:
            messages.error(request, 'Неверные данные')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request,'Вы вышли.')
        return redirect('index')

@login_required(login_url='/accounts/signup')
def userprofile(request):
    try:
        profile = Profile.objects.create(user_id=request.user.id) 
        profile.save()
        profile = get_object_or_404(Profile, pk=request.user.profile.id)
    except IntegrityError:
        profile = get_object_or_404(Profile, pk=request.user.profile.id)
    return render(request, 'accounts/userprofile.html',{'profile':profile})

def gotoedit(request):
    return render(request,'accounts/useredit.html') 
@login_required(login_url='/accounts/signup')
def edit(request):
    if request.method == 'POST':
        if request.POST['about']:
                profile = Profile.objects.get(user_id=request.user.id)
                profile.about = request.POST['about']
                try:
                    profile.avatar = request.FILES['image']
                except:
                    pass
                else:
                    profile.avatar = request.FILES['image']
                profile.save()
                return redirect('userprofile')





