"""
Serializers for Content, Tags and it's relation
"""

from rest_framework.serializers import ModelSerializer, SlugRelatedField
from linkitos.models import Content, Tag


class ContentSerializer(ModelSerializer):
    """
    Content serializer
    """
    tags = SlugRelatedField(many=True,
                            read_only=True,
                            slug_field='name')

    class Meta:
        model = Content
        fields = "__all__"


class TagSerializer(ModelSerializer):
    """
    Tag Serializer
    """
    class Meta:
        model = Tag
        fields = "__all__"
