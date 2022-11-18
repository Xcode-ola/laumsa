from django.shortcuts import render
from .serializer import *
from .models import ChapterList, Question, contact_details, CourseList, CourseSummary, Quiz
from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.test import APIRequestFactory
from rest_framework.request import Request
from rest_framework.pagination import PageNumberPagination

# Create your views here.
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    def get_paginated_response(self, data):
        return Response({
            'page_size': self.page_size,
            'total_objects': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'current_page_number': self.page.number,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data,
        })

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
        factory = APIRequestFactory()
        request = factory.get('/')
        serializer_context = {'request':Request(request)}
        question = CourseSummary.objects.filter(course__name = kwargs['name']).filter(chapter__slug = kwargs['slug_field'])
        serializer = SummaryPageSerializer(instance=question, many=True, context=serializer_context)
        return Response(serializer.data)

class QuizHomePage(generics.ListAPIView):
    queryset = CourseList.objects.all()
    serializer_class = QuizHomePageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class QuizListPage(APIView):
    def get(self, request, format=None, **kwargs):
        question = Quiz.objects.filter(course__name = kwargs['name'])
        serializer = QuizListSerializer(question, many=True)
        return Response(serializer.data)

class StartQuiz(APIView):
    permission_classes = [permissions.IsAuthenticated]
    pagination_classes = [PageNumberPagination()]
    def get(self, request, format=None, **kwargs):
        question = Question.objects.filter(chapter__id = kwargs['pk']).order_by('?')[:100]
        serializer = QuizSerializer(question, many=True)
        return Response(serializer.data)