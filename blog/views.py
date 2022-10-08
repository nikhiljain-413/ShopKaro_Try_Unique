from django.shortcuts import render
from .models import Blogpost
from django.http import HttpResponse
# Create your views here.

# def index(request):
#     # return HttpResponse("<h1>Index Blog</h1>")
#     # return render(request, 'indexblog.html')
#     return render(request, 'blog/index.html')

def index(request):
    myposts = Blogpost.objects.all()
    print(myposts)
    return render(request, 'blog/index.html',
                  {'myposts': myposts})

def blogpost(request, id):
    post = Blogpost.objects.filter(post_id = id)[0]
    print(post)
    return render(request, 'blog/blogpost.html',
                  {'post':post})