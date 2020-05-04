from django.shortcuts import render

from .models import post


def home(request):
    context = {

        'post': post.objects.all()
    }
    return render(request, 'blog/home.html',context)


def about(request):
    return render(request, 'blog/about.html',{'title':'about'})
