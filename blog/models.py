import os

from django.db import models
from django.urls import reverse
from markdownx.models import MarkdownxField
from markdownx.utils import markdown
from core import models as core_models
# FIXME custom user로 수정
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:tag', args=[self.slug])

    class Meta:
        verbose_name_plural = '태그'


class Category(core_models.DateTime):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:category', args=[self.slug])

    class Meta:
        verbose_name_plural = '카테고리'


class Post(core_models.DateTime):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tag, blank=True)
    title = models.CharField(max_length=30)
    content = MarkdownxField()
    hook_text = models.CharField(max_length=100, blank=True)
    head_image = models.ImageField(blank=True, upload_to='blog/images/%Y/%m/%d/')
    file_upload = models.FileField(blank=True, upload_to='blog/files/%Y/%m/%d/')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', args=[self.id])

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]

    def get_content_markdown(self):
        return markdown(self.content)

    class Meta:
        verbose_name_plural = '게시글'


class Comment(core_models.DateTime):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return f'{self.author}::{self.content}'

    def get_absolute_url(self):
        return f'{self.post.get_absolute_url()}#comment-{self.pk}'

    def get_avatar_url(self):
        if self.author.socialaccount_set.exists():
            return self.author.socialaccount_set.first().get_avatar_url()
        else:
            return 'http://placehold.it/50x50'

    class Meta:
        verbose_name_plural = '댓글'
