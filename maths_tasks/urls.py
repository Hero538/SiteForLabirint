from django.urls import path
from . import views

urlpatterns = [
    path('',views.maths_tasks,name='maths_tasks') #что я делаю?

]
