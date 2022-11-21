from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

User = get_user_model()

@login_required(login_url='/user/login/')
def me(request):
    return render(request, 'me.html', {'user': request.user})

def another_user(request, user_id): 
    return render(request, 'me.html', {'user': User.objects.get(pk=user_id)})


def user_login(request):
    return render(request, 'login.html')

def user_register(request): 
    return render(request, 'register.html')