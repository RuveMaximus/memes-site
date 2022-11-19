from django.shortcuts import render, redirect
from .forms import PostForm

def index(request): 
    form = PostForm()
    return render(request, 'index.html', {'form': form})

def publish(request):
    form = PostForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('/feed')