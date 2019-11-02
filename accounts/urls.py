from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.register,name='register'),
    #path('setprofile/',views.setprofile,name='setprofile'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('profile/', views.userprofile, name='userprofile'),
    path('profile/gotoedit', views.gotoedit, name='gotoedit'),
    path('profile/edit', views.edit, name='edit'),

]