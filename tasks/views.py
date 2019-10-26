from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages



# Create your views here.
main_variables=['F','S','U','Q']
other_vars=['m','a','c','m','t','v','V','p'] 
def tasks(request):
    if request.method == 'POST':
        varname = request.POST['varname'] 
        varcount= request.POST['varcount']
        varname2 = request.POST['varname2']
        varcount2= request.POST['varcount2']
        varfind= request.POST['varfind'] 
        if varname not in main_variables or varname2 not in main_variables or varfind not in main_variables or varname not in other_vars or varname2 not in other_vars or varfind not in other_vars:
            messages.error(request, 'Неверные данные')
            return redirect('tasks') #почему таскс? потому что я дебил дурак боюсь менять переменную
        if varfind in main_variables:
            try:
                tasks=varcount//varcount2
            except (ZeroDivisionError, TypeError, NameError):
                messages.error(request, 'Неверные данные')
            tasks=varcount*varcount2
        else:
            if varname in main_variables:
                try:
                    tasks=varcount//varcount2
                except (ZeroDivisionError, TypeError, NameError):
                    messages.error(request, 'Неверные данные')
                tasks=varcount//varcount2
            else:
                try:
                    tasks=varcount2//varcount
                except (ZeroDivisionError, TypeError, NameError):
                    messages.error(request, 'Неверные данные')
                tasks=varcount2//varcount
        if tasks is not None:
            return render(request, 'tasks.html', {'tasks': tasks})
        else:
            messages.error(request, 'Неверные данные')
            return redirect('tasks')
    else:

        return render(request, 'tasks.html', {'tasks': tasks})
