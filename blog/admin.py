from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Post, Category, Tag, Comment


@admin.register(Post)
class PostAdmin(MarkdownxModelAdmin):
    list_display = ('id', 'title', 'author', 'created_at')
    list_display_links = ('title',)
    # fields = ('title', 'content', 'created_at', 'updated_at')
    # readonly_fields = ('created_at', 'updated_at')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
