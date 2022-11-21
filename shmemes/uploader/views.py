from django.shortcuts import render, redirect
from .forms import PostForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='/user/login/')
def uploader(request): 
    form = PostForm()
    return render(request, 'uploader.html', {'form': form})

@login_required(login_url='/user/login/')
def publish(request):
    form = PostForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('/feed')