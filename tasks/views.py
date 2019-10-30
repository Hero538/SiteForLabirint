from django.shortcuts import render,redirect, HttpResponse
from django.contrib import messages



# Create your views here.
main_variables=['F','S','U'] #))
other_vars=['a','m','t','v'] 
def tasks(request):
    answer=None
    if request.method == 'POST':
        varname = request.POST['varname'] 
        varcount= request.POST['varcount']
        varname2 = request.POST['varname2']
        varcount2= request.POST['varcount2']
        varfind= request.POST['varfind'] 
        #if varname not in main_variables or varname2 not in main_variables or varfind not in main_variables or varname not in other_vars or varname2 not in other_vars or varfind not in other_vars:
         #   messages.error(request, 'Неверные данные')
          #  return redirect('tasks') 
        if varfind in main_variables:
            try:
                answer=varcount*varcount2
            except (ZeroDivisionError, TypeError, NameError):
                messages.error(request, 'Неверные данные')
            else:
                answer=varcount*varcount2
                answer.save()
                return render(request, 'tasks.html', {'tasks': answer})
        elif varfind in other_vars :
            try:
                answer=varcount//varcount2
            except (ZeroDivisionError, TypeError, NameError):
                messages.error(request, 'Неверные данные')
            else:
                answer=varcount//varcount2
                answer.save()
                return render(request, 'tasks.html', {'tasks': answer})
        else:
            try:
                answer=varcount2//varcount
            except (ZeroDivisionError, TypeError, NameError):
                messages.error(request, 'Неверные данные')
            else:
                answer=varcount2//varcount
                answer.save()
                return render(request, 'tasks.html', {'tasks': answer})
        if answer is not None:
            return render(request, 'tasks.html', {'tasks': answer})
        else:
            messages.error(request, 'Неверные данные')
            return redirect('tasks')
    else:

        return render(request, 'tasks.html')