from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import get_user_model


User = get_user_model()


def me(request):
    return render(request, 'me.html', {'user': User.objects.get(pk=request.user.pk)})

def another_user(request, user_id): 
    return render(request, 'me.html', {'user': User.objects.get(pk=user_id)})