from django.urls import path
from . import views

urlpatterns = [
    path('',views.forum,name='forum'),
    path('add/',views.add,name='add'),
    path('<int:post_id>',views.details,name='details'),
]