from django.db import models
from django.utils.timezone import now


class Location(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField()

    class Meta(object):
        ordering = ['name']

    def __str__(self):
        return self.name


class Screen(models.Model):
    file_name = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)
    location = models.ManyToManyField(Location)
    priority = models.PositiveSmallIntegerField(default=0)
    seconds = models.PositiveSmallIntegerField(default=60)
    text = models.CharField(max_length=100, blank=True, null=True)
    video_url = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    start_date = models.DateTimeField(default=now)
    due_date = models.DateTimeField(default=now)
    is_video = models.BooleanField(default=False)

    class Meta(object):
        ordering = ['priority', '-modified_at', '-created_at']

    def __str__(self):
        return self.file_name
