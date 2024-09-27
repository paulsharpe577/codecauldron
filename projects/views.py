# projects/views.py

from django.http import HttpResponseRedirect
from django.shortcuts import render
from projects.models import Project, Comment
from blog.forms import CommentForm

def project_index(request):
    projects = Project.objects.all()
    context = {
        "projects": projects,
    }
    return render(request, "projects/project_index.html", context)


def project_category(request, category):
    projects = Project.objects.filter(
        categories__name__contains=category
    ).order_by("-created_on")
    context = {
        "category": category,
        "projects": projects,
    }
    return render(request, "projects/category.html", context)


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)

    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                project=project,
            )
            comment.save()
            return HttpResponseRedirect(request.path_info)
    comments = Comment.objects.filter(project=project).order_by("-created_on")
    context = {
        "project": project,
        "comments": comments,
        "form": CommentForm(),
    }

    return render(request, "projects/project_detail.html", context)
