from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('userprofile/', views.userprofile, name='userprofile'),
    path('useredit/', views.edit, name='edit'),
    path('gotoedit/', views.gotoedit, name='gotoedit')
]