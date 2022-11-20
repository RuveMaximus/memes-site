from django.urls import path

from . import views
from . import controller

urlpatterns = [
    path('me/', views.me, name='me'),
    path('<int:user_id>/', views.another_user),

    path('login/', controller.user_login, name='login'),
    path('logout/', controller.user_logout, name='logout'),
    path('register/', controller.user_register, name='registration'),
]