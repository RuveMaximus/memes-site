from django.shortcuts import render
from django.http import JsonResponse
from .models import Post

# Create your views here.

def feed(request):
    posts = Post.objects.all().order_by('pub_date')[::-1]
    return render(request, 'feed.html', {
        "posts": posts
    })