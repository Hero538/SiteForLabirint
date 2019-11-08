from django.shortcuts import render, get_object_or_404
from .models import Tiding
from django.db.models import Q
# Create your views here.
def index(request):
    search_query = request.GET.get('search', '')
    if search_query:
        tidings = Tiding.objects.filter(Q(title__icontains=search_query) | Q(body__icontains=search_query))

    else:
        tidings = Tiding.objects.order_by('-pub_date').filter(is_published=True)
    return render(request, 'pages/index.html', {'tidings': tidings})

def details(request,tiding_id):
    tiding = get_object_or_404(Tiding,pk=tiding_id)
    return render(request,'pages/details_m.html',{'tiding':tiding})

def task(request):
    return render(request, 'pages/../templates/tasks/tasks.html')