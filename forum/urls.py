from django.urls import path
from . import views

urlpatterns = [
    path('',views.forum,name='forum'),
    path('add/',views.add,name='add'),
    path('<int:post_id>/',views.details,name='details'),
    path('<post_id>/upvote/',views.upvote,name='upvote'),
    path('<post_id>/downvote/',views.downvote,name='downvote'),
    path('<int:post_id>/comment/',views.add_comment,name='add_comment'),
]