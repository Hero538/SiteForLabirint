from django.shortcuts import render,redirect, HttpResponse
from django.contrib import messages



# Create your views here.
main_variables=['F','S','U'] #))
other_vars=['a','m','t','v', 'I', 'R'] 
def tasks(request):
    answer=None
    if request.method == 'POST':
        varname = request.POST['varname'] 
        varcount= int(request.POST['varcount'])
        #varname2 = request.POST['varname2']
        varcount2= int(request.POST['varcount2'])
        varfind= request.POST['varfind'] 
        try:
            answer=varcount2/varcount
        except (ZeroDivisionError, TypeError, NameError):
             messages.error(request, 'Неверные данные')
        else:
            if varfind in main_variables:
                answer=varcount*varcount2
                return render(request, 'tasks/tasks.html', {'tasks': answer})
            elif varfind in other_vars :    
                if varname in main_variables:
                    answer=varcount/varcount2
                    return render(request, 'tasks/tasks.html', {'tasks': answer})
                else:
                    answer=varcount2/varcount
                    return render(request, 'tasks/tasks.html', {'tasks': answer})
        if answer is not None:
            return render(request, 'tasks/tasks.html', {'tasks': answer})
        else:
            messages.error(request, 'Неверные данные')
            return redirect('tasks')
    else:

        return render(request, 'tasks/tasks.html')