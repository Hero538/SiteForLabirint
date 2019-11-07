from django.urls import path
from . import views

urlpatterns = [
    path('',views.informatics_tasks,name='informatics_tasks') 

]
