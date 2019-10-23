from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'pages/index.html')

def task(request):
    return render(request, 'pages/../templates/tasks/tasks.html')