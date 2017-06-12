"""
Serializers for Content, Tags and it's relation
"""

from rest_framework.serializers import (ModelSerializer, SlugRelatedField,
                                        ReadOnlyField, HyperlinkedModelSerializer)
from linkitos.models import Content, Tag, ContentTag


class ContentTagSerializer(HyperlinkedModelSerializer):
    """
    Content-Tag Relation Serializer
    """
    name = ReadOnlyField(source='tag.name')

    class Meta:
        model = ContentTag
        fields = ('name', 'linked_at')


class ContentSerializer(ModelSerializer):
    """
    Content serializer
    """
    tags = ContentTagSerializer(source='contenttag_set',
                                many=True,
                                read_only=True)

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
