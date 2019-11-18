from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages

# Create your views here.
def somesystem(N, base):
    if not hasattr(somesystem, 'table'):        
        somesystem.table = '0123456789ABCDEF'       
    n, num = divmod(N, base)        
    return somesystem(n, base) + somesystem.table[num] if n else somesystem.table[num] 

def informatics_tasks(request):
    if request.method == 'POST':
        num = int(request.POST['num'])
        n = int(request.POST['n'])
        answer=somesystem(n, num)
        if answer is not None:
            return render(request, 'informatics_tasks/informatics_tasks.html', {'answer': answer})
        else:
            answer = 'Пусто'
            return redirect('informatics_tasks')
    else:
        return render(request, 'informatics_tasks/informatics_tasks.html')
