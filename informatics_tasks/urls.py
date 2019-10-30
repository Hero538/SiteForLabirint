from django.urls import path
from . import views

urlpatterns = [
    path('informatics_tasks/',views.informatics_tasks,name='informatics_tasks') 

]
