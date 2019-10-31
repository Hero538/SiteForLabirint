from django.urls import path
from . import views

urlpatterns = [
    path('', views.search, name='index'), #ничего не делает потому что ничто ничего не делает
]