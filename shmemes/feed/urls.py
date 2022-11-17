from django.urls import path

from . import views, controller

urlpatterns = [
    path('', views.feed),
    
    path('addcomment/', controller.add_comment),
    path('getcomments/', controller.get_comments),
]