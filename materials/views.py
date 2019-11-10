from django.shortcuts import render
from bs4 import BeautifulSoup

# Create your views here.
def materials(request):
    return render(request,'materials/materials.html')

def mechanics(request):
    return render(request,'materials/physics/mechanics/mechanics.html')

def kinematics(request):
    return render(request,'materials/physics/kinematics/kinematics.html')

def dynamics(request):
    return render(request,'materials/physics/dynamics/dynamics.html')

def search(request): #скачиваю интернет! точнее собираюсь скачять, потом доделаю
    #суть в том, что я упарываюсь и прогоняю с помощью bs4 каждый html и возвращаю тот, в котором содержится поисковой запрос
    #возможно, это абсурдно
    search_query = request.GET.get('search', '')
    mechanics = render(request,'materials/physics/mechanics/mechanics.html') 

    
        
        



    