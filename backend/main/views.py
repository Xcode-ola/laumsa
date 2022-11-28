from django.shortcuts import render
from .serializer import *
from .permissions import *
from .models import ChapterList, Question, contact_details, CourseList, CourseSummary, Quiz
from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.test import APIRequestFactory
from rest_framework.request import Request
from rest_framework.pagination import PageNumberPagination

# Create your views here.
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 25
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
    permission_classes = [permissions.IsAuthenticated]

class ContactPage(generics.ListCreateAPIView):
    queryset = contact_details.objects.all()
    serializer_class = ContactPageSerializer
    permission_classes = [permissions.IsAdminUser]

class Chapters(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request, format=None, **kwargs):
        #factory = APIRequestFactory()
        #request = factory.get('https://localhost:8000/course/<str:name>/')
        #serializer_context = {'request':Request(request)}
        question = ChapterList.objects.filter(course__name = kwargs['name'])
        serializer = ChapterListSerializer(question, many=True)
        return Response(serializer.data)

class SummaryPage(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request, format=None, **kwargs):
        question = CourseSummary.objects.filter(course__name = kwargs['name']).filter(chapter__slug = kwargs['slug_field'])
        summary = question.filter(isverified=True)
        serializer = SummaryPageSerializer(instance=summary, many=True)
        return Response(serializer.data)

class QuizHomePage(generics.ListAPIView):
    queryset = CourseList.objects.all()
    serializer_class = QuizHomePageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class QuizListPage(APIView):
    def get(self, request, format=None, **kwargs):
        factory = APIRequestFactory()
        #request = factory.get('http://127.0.0.1:8000/start_quiz/<int:pk>/')
        #request = factory.get('http://127.0.0.1:8000/start_quiz/')
        #serializer_context = {'request':Request(request)}
        quiz = Quiz.objects.filter(course__name = kwargs['name'])
        serializer = QuizListSerializer(quiz, many=True,)
        return Response(serializer.data)

class StartQuiz(APIView):
    permission_classes = [permissions.IsAuthenticated]
    pagination_classes = [PageNumberPagination()]
    def get(self, request, format=None, **kwargs):
        question = Question.objects.filter(quiz__id = kwargs['pk']).order_by('?')[:100]
        serializer = QuizSerializer(question, many=True)
        return Response(serializer.data)

class PracticeQuestionPage(APIView):
    permission_classes = [permissions.IsAuthenticated]
    pagination_classes = [StandardResultsSetPagination()]
    def get(self, request, format=None, **kwargs):
        question = PracticeQuestion.objects.filter(course__name = kwargs['name']).filter(chapter__slug = kwargs['slug_field'])
        serializer = TheorySerializer(question, many=True)
        return Response(serializer.data)

class PracticeQuestionList(APIView):
    permission_classes = [permissions.IsAuthenticated]
    pagination_classes = [StandardResultsSetPagination()]
    def get(self, request, format=None, **kwargs):
        question = PracticeQuestion.objects.filter(course__name = kwargs['name'])
        serializer = TheorySerializer(question, many=True)
        return Response(serializer.data)
