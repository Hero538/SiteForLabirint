from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
# Create your views here.


def materials(request):
    return render(request, 'materials/materials.html')


def physics(request):
    return render(request, 'materials/physics/physics.html')
