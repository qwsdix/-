from django.http import HttpResponse
from django.shortcuts import render

from blog.models import Category, Post


def index(request):
    categories = Category.objects.all()
    posts = Post.objects.all()

    context = {
        'categories': categories,
        'posts': posts,
    }

    return render(
        request,
        'blog/index.html',
        context,
    )
