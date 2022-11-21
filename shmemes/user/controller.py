from django.contrib.auth import login, logout, authenticate
from django.http import JsonResponse
from django.contrib.auth.models import User

from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def user_login(request):
    data = json.loads(request.body.decode('utf-8'))

    username = data.get('username')
    password = data.get('password')

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return JsonResponse({'status': 'ok'})
    
    return JsonResponse({'status': 'fail'})

@csrf_exempt
def user_logout(request): 
    logout(request)

    return JsonResponse({'status': 'ok'})

@csrf_exempt
def user_register(request):
    data = json.loads(request.body.decode('utf-8'))

    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    try: 
        User.objects.get(username=username)
        return JsonResponse({'status': 'fail'})

    except User.DoesNotExist:
        user = User.objects.create_user(username, email, password)
        user.save()

        return JsonResponse({'status': 'ok'})
