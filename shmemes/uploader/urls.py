from django.urls import path

from . import views

urlpatterns = [
    path('', views.uploader, name='uploader'),
    path('publish/', views.publish, name="publish"),
]