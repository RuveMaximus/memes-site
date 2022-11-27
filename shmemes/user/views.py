from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from feed.models import Post

User = get_user_model()

@login_required(login_url='/user/login/')
def me(request):
    posts = Post.objects.filter(author=request.user)
    post_count = posts.count()
    return render(request, 'me.html', {
        'user': request.user, 
        'posts': posts.order_by('pub_date')[::-1], 
        'post_count': post_count,
    })

def another_user(request, user_id): 
    user = User.objects.get(pk=user_id)
    posts = Post.objects.filter(author=user)
    post_count = posts.count()
    return render(request, 'me.html', {
        'user': request.user, 
        'posts': posts.order_by('pub_date')[::-1], 
        'post_count': post_count,
    })


def user_login(request):
    return render(request, 'login.html')

def user_register(request): 
    return render(request, 'register.html')