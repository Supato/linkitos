"""
Models containing Content (links), Tags, Relations
"""

from django.db import models

class Content(models.Model):
    """
    Content model
    """
    url = models.URLField(blank=True, null=True)
    description = models.CharField(max_length=2048, blank=True)
    tags = models.ManyToManyField('Tag', through='ContentTag')
    created_at = models.DateTimeField(auto_now_add=True)


class Tag(models.Model):
    """
    Tag model
    """
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=2048, blank=True)


class ContentTag(models.Model):
    """
    Link between Content and Tags

    enables adding extra fields like assignee, date, etc
    """
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("content", "tag")
