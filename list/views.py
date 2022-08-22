from django.shortcuts import render
from list.models import Post



def post_list(request):
    posts = Post.objects.all()
    context = {'post_list' : posts}
    return render(request, "list/propozycje.html", context)
