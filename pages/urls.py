from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('details/<int:tiding_id>/',views.details,name='details_m'),
]