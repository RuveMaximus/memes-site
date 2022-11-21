from django.urls import path

from . import views
from . import controller

urlpatterns = [
    path('me/', views.me, name='me'),
    path('<int:user_id>/', views.another_user),

    path('login/', views.user_login, name='login'),
    path('register/', views.user_register, name='registration'),

    path('api/login/', controller.user_login),
    path('api/logout/', controller.user_logout),
    path('api/register/', controller.user_register),
]