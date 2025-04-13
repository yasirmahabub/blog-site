from django.contrib import admin

from posts.models import Comment, Post


class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "publish_date")


admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "post")


admin.site.register(Comment, CommentAdmin)
