from django.shortcuts import render

from .models import Post


def home_view(request):
    """
    Display the list of blog posts on the home page
    """

    # Get the 5 most recent posts from the database
    posts = Post.objects.order_by("-id")[:5]

    context = {"posts": posts}
    return render(request, "home.html", context)
