from django.shortcuts import render
from .models import Post


def index(request):
    return render(request, 'page.html', {'posts': Post.objects.filter(page=1), 'title': 'Home page'})


def about(request):
    return render(request, 'page.html', {'posts': Post.objects.filter(page=2), 'title': 'About us'})


def algorithm(request):
    return render(request, 'page.html', {'posts': Post.objects.filter(page=3), 'title': 'How can you help'})


def stories(request):
    return render(request, 'page.html', {'posts': Post.objects.filter(page=4), 'title': "Beggars' lives"})


def faq(request):
    return render(request, 'page.html', {'posts': Post.objects.filter(page=5), 'title': "Questions & Answers"})
