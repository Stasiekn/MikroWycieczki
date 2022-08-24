from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Post
from django.template import loader


def post_details(request, post_id):
    post = Post.objects.get(pk=post_id)
    context = {'post': post}
    return render(request, "posts/details_post.html", context)

def posts_list(request):
    posts = Post.objects.all()
    context = {'post_list': posts}
    return render(request, "posts/list.html", context)

# Create your views here.
