from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages

# Create your views here.
def informatics_tasks(request):
    if request.method == 'POST':
        num = int(request.POST['num'])
        n = request.POST['n']
        #try:
         #   answer=int(num, n) #не работает
        #except BaseException:  
         #   messages.error(request, 'баз экспешн)')
          #  return redirect('informatics_tasks')
        #else:
        answer=int(n, num)
        if answer is not None:
            return render(request, 'informatics_tasks.html', {'answer': answer})
            #answer.save()
        else:
            messages.error(request, 'Пусто')
            return redirect('informatics_tasks')
    else:
        return render(request, 'informatics_tasks.html')
