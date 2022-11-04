from django.shortcuts import render
from .serializer import ChapterListSerializer, ContactPageSerializer, IndexPageSerializer, SummaryPageSerializer
from .models import ChapterList, contact_details, CourseList, CourseSummary
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class IndexPage(generics.ListCreateAPIView):
    queryset = CourseList.objects.all()
    serializer_class = IndexPageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ContactPage(generics.ListCreateAPIView):
    queryset = contact_details.objects.all()
    serializer_class = ContactPageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class Chapters(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request, format=None, **kwargs):
        question = ChapterList.objects.filter(course__name = kwargs['name'])
        serializer = ChapterListSerializer(question, many=True)
        return Response(serializer.data)

class SummaryPage(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request, format=None, **kwargs):
        question = CourseSummary.objects.filter(course__name = kwargs['name']).filter(chapter__slug = kwargs['slug_field'])
        serializer = SummaryPageSerializer(question, many=True)
        return Response(serializer.data)