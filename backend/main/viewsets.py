from rest_framework import viewsets
from .serializer import ChapterListSerializer, ContactPageSerializer, IndexPageSerializer, SummaryPageSerializer
from .models import ChapterList, contact_details, CourseList, CourseSummary
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.test import APIRequestFactory
from rest_framework.request import Request

class ChapterViewSet(viewsets.ViewSet):
    def get(self, request, format=None, **kwargs):
        factory = APIRequestFactory()
        request = factory.get('/')
        serializer_context = {'request':Request(request)}
        question = CourseSummary.objects.filter(course__name = kwargs['name']).filter(chapter__slug = kwargs['slug_field'])
        serializer = SummaryPageSerializer(instance=question, many=True, context=serializer_context)
        return Response(serializer.data)
