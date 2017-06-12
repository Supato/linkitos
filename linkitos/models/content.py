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

    def __str__(self):
        return self.url


class Tag(models.Model):
    """
    Tag model
    """
    name = models.CharField(max_length=128, unique=True)
    description = models.CharField(max_length=2048, blank=True)

    def __str__(self):
        return self.name


class ContentTag(models.Model):
    """
    Link between Content and Tags

    enables adding extra fields like assignee, date, etc
    """
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    linked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("content", "tag")

    def __str__(self):
        return "{} - {}".format(self.content, self.tag)
