from django.urls import path
from . import views

urlpatterns = [
    path('materials/',views.materials,name='materials'),
    path('materials/physics/mechanics/', views.mechanics, name='mechanics'),
    path('materials/physics/kinematics/', views.kinematics, name='kinematics')

]