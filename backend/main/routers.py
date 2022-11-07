from xml.etree.ElementInclude import include
from rest_framework.routers import DefaultRouter
from .viewsets import ChapterViewSet

router = DefaultRouter()
router.register('<str:name>/<str:slug_field>/', ChapterViewSet, basename='chapter')
urlpatterns = router.urls