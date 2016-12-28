from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Post


def posts_create(request):
    return HttpResponse("<h1>Create</h1>")


def posts_detail(request, id=None):
    instance = get_object_or_404(Post, id=id)
    context = {
        "title": "Detail",
        "instance": instance
    }
    return render(request, "post_detail.html", context)


def posts_list(request):
    queryset = Post.objects.all()
    # if request.user.is_authenticated():
    #     context = {
    #         "title": "My User list"
    #     }
    # else:
    context = {
        "object_list": queryset,
        "title": "List"
    }
    return render(request, "index.html", context)


def posts_update(request):
    return HttpResponse("<h1>Update</h1>")


def posts_delete(request):
    return HttpResponse("<h1>Delete</h1>")
