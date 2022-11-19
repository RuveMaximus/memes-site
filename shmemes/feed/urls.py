from django.urls import path

from . import views, controller

urlpatterns = [
    path('', views.feed, name='feed'),

    path('addpost/', controller.add_post),
    
    path('addcomment/', controller.add_comment),
    path('getcomments/', controller.get_comments),
]