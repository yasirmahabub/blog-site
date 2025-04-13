from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from posts.views import home_view, post_detail_view, post_list_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_view, name="home"),
    path("posts/", post_list_view, name="post-list"),
    path("posts/<int:post_id>", post_detail_view, name="post-detail"),
]


if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]
