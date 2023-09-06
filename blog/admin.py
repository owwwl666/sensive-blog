from django.contrib import admin
from blog.models import Post, Tag, Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author']
    raw_id_fields = ['author']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    raw_id_fields = [
        'author',
        'likes',
        'tags'
    ]


admin.site.register(Tag)
