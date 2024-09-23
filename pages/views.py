# pages/views.py

from django.shortcuts import render
from blog.models import Post

#def home(request):
#    return render(request, "pages/home.html", {})
def home(request):
    posts = Post.objects.filter(featured=True).order_by("-created_on")
    context = {
        "posts": posts,
    }
    return render(request, "pages/home.html", context)


def calendar(request):
    return render(request, "pages/calendar.html", {})

