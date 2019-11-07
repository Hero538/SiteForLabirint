from django.shortcuts import render

# Create your views here.
def materials(request):
    return render(request,'materials/materials.html')

def mechanics(request):
    return render(request,'materials/physics/mechanics/mechanics.html')

def kinematics(request):
    return render(request,'materials/physics/kinematics/kinematics.html')

def dynamics(request):
    return render(request,'materials/physics/dynamics/dynamics.html')
    