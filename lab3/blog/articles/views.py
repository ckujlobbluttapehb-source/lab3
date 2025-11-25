from django.shortcuts import render
from .models import Article

def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all()})

def hello(request):
    return HttpResponse('Привет, Мир! (страница hello)')