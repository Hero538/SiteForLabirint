from django.urls import path
from . import views

urlpatterns = [
    path('materials/',views.materials,name='materials'),
    path('materials/physics/', views.physics, name='physics'),

]