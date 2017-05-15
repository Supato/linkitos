"""
Django Admin customizations
"""

from django.contrib import admin
from linkitos.models import Tag, Content, ContentTag

admin.site.register(Tag)
admin.site.register(Content)
admin.site.register(ContentTag)
