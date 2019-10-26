from django.urls import path
from . import views

urlpatterns = [
    path('',views.informatics_tasks,name='some_system') #я запуталась в зависимостях помогите 

]
