from django.shortcuts import get_object_or_404, render

from .models import Comment, Post


def home_view(request):
    """
    Display a list of recent blog posts on the home page
    """

    # Get the 5 most recent posts from the database
    posts = Post.objects.order_by("-id")[:5]

    context = {"posts": posts}
    return render(request, "home.html", context)


def post_list_view(request):
    """
    Display a list of all blog posts
    """

    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, "post_list.html", context)


def post_detail_view(request, post_id):
    """
    Display the detail view of a specific blog post, including its comments.

    Retrieves the blog post by its ID and fetches all related comments,
    including user data for each comment, to optimize query performance.

    Args:
        request (HttpRequest): The incoming HTTP request object.
        post_id (int): The ID of the blog post to retrieve.

    Returns:
        HttpResponse: The rendered detail page for the specified blog post.
    """

    post = get_object_or_404(Post, id=post_id)
    comments = Comment.objects.filter(post_id=post_id).select_related("user")

    context = {"post": post, "comments": comments}
    return render(request, "post_detail.html", context)
