"""
URLs dispatcher
"""

import logging
from django.conf.urls import url, include
from rest_framework.routers import SimpleRouter
from linkitos import views

logger = logging.getLogger(__name__)

api_router = SimpleRouter()
api_router.register(r'content', views.ContentViewSet)
api_router.register(r'tag', views.TagViewSet)

urlpatterns = [
    url(r'^$', views.HelloView.as_view(), name="index"),
    url(r'^api/1/', include(api_router.urls))
]
