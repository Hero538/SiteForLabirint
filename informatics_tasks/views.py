from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages

# Create your views here.
def binary_system(request):
    if request.method == 'POST':
    varname = request.POST['varname'] 
    try:
  	  inftasks=bin(int(varname))[2:]
	except ValueError, TypeError, NameError:
		messages.error(request, 'Неверные данные')
		return redirect('tasks')
	inftasks=bin(int(varname))[2:]
	if tasks is not None:
		return render(request, 'informatics_tasks.html', {'inftasks': inftasks})
	else:
		messages.error(request, 'Неверные данные')
		return redirect('tasks')
    else:
        return render(request, 'informatics_tasks.html', {'inftasks': inftasks})
    