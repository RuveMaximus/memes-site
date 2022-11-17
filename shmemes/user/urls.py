from django.urls import path

from . import views

urlpatterns = [
    path('me/', views.me, name='me'),
    path('<int:user_id>/', views.another_user)
]