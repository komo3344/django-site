import os

from django.db import models
from core import models as core_models


class Post(core_models.DateTime):
    title = models.CharField(max_length=30)
    content = models.TextField()
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
