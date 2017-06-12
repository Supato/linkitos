"""
Views related to contents
"""

from rest_framework.viewsets import ModelViewSet
from linkitos.models import Content, Tag
from linkitos.serializers import ContentSerializer, TagSerializer


class ContentViewSet(ModelViewSet):
    """
    Content API Views
    """
    queryset = Content.objects.all()
    serializer_class = ContentSerializer


class TagViewSet(ModelViewSet):
    """
    Tag API Views
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
