from django.contrib.auth import login, logout, authenticate
from django.http import JsonResponse
from django.contrib.auth.models import User


def user_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'fail'})


def user_logout(request): 
    logout(request)

    JsonResponse({'status': 'ok'})


def user_register(request):
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')

    user = User.objects.create_user(username, email, password)
    user.save()

    return JsonResponse({'status': 'ok'})
