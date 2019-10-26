from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages

# Create your views here.
def some_system(request):
    if request.method == 'POST':
        num = request.POST['num'] 
        n = request.POST['n'] 
        try:
            answer=int(num, n) #я серьезно, оно так работает!
        except BaseException:  
            messages.error(request, 'Неверные данные')
            return redirect('informatics_tasks')
        else:
            answer=int(num, n)
        if answer is not None:
            return render(request, 'informatics_tasks.html', {'answer': answer})
        else:
            messages.error(request, 'Неверные данные')
            return redirect('informatics_tasks')
    else:
        return render(request, 'informatics_tasks.html')
