from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def feed(request):
    return render(request, 'feed.html', {
        "posts": [
            {"title": 'First post', 'description': 'Hello world, description'},
            {"title": 'Second post', 'description': 'Description for second post'}
        ]
    })