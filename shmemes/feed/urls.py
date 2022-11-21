from django.urls import path

from . import views, controller

urlpatterns = [
    path('', views.feed, name='feed'),
    
    path('addcomment/', controller.add_comment),
    path('getcomments/', controller.get_comments),

    path('api/like/', controller.like),
    path('api/dislike/', controller.dislike),
]