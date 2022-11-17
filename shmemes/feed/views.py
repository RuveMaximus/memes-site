from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def feed(request):
    return render(request, 'feed.html')