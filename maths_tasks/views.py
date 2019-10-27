from django.shortcuts import render,redirect
from django.contrib import messages

# Create your views here.
def fac(n):
    if n == 0:
        return 1
    return fac(n-1) * n 

print(fac(5))
#actions=['P', 'A', 'C']
def permutations(request):
    if request.method == 'POST':
        action = request.POST['action']
        n = request.POST['n']
        k = request.POST['k']
        if action=='P':
            try:
                answer=fac(n)
            except (ZeroDivisionError, TypeError, NameError):
                messages.error(request, 'Неверные данные')
            else:
                answer=fac(n)
        elif action=='A':
            try:
                answer=fac(n)//fac(n-k)
            except (ZeroDivisionError, TypeError, NameError):
                messages.error(request, 'Неверные данные')
            else:
                answer=fac(n)//fac(n-k)
        elif action=='C':
            try:
                answer=fac(n)//(fac(n-k)*fac(k))
            except (ZeroDivisionError, TypeError, NameError):
                messages.error(request, 'Неверные данные')
            else:
                answer=fac(n)//(fac(n-k)*fac(k))
        else:
            messages.error(request, 'Неверные данные')
            return redirect('maths_tasks') 
            
        if answer is not None:
            return render(request, 'maths_tasks.html', {'tasks': answer})
        else:
            messages.error(request, 'Неверные данные')
            return redirect('maths_tasks')
    else:

        return render(request, 'maths_tasks.html')
