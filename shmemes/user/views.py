from django.shortcuts import render
from django.http import HttpResponse


def me(request):
    return render(request, 'me.html', {'user': 'Вася Пупкин'})
