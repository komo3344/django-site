import os

from django.db import models
from core import models as core_models
# FIXME custom user로 수정
from django.contrib.auth.models import User


class Category(core_models.DateTime):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/blog/category/{self.slug}/'

    class Meta:
        verbose_name_plural = '카테고리'


class Post(core_models.DateTime):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=30)
    content = models.TextField()
    hook_text = models.CharField(max_length=100, blank=True)
    head_image = models.ImageField(blank=True, upload_to='blog/images/%Y/%m/%d/')
    file_upload = models.FileField(blank=True, upload_to='blog/files/%Y/%m/%d/')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]

    class Meta:
        verbose_name_plural = '게시글'
