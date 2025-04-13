from django.contrib import admin
from django.urls import path

from posts.views import home_view, post_list_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_view, name="home"),
    path("posts/", post_list_view, name="post-list"),
]
