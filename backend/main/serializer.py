from rest_framework import serializers
from .models import CourseList, Quiz, contact_details, ChapterList, CourseSummary, Question, Answer

#homepage serializer for the website. The page contains all the courses and a link to the contact address
class IndexPageSerializer(serializers.ModelSerializer):
    chapter = serializers.HyperlinkedIdentityField(view_name='chapter',lookup_field = "name")
    quiz = serializers.HyperlinkedIdentityField(view_name='quiz_list',lookup_field = "name")
    class Meta:
        model = CourseList
        fields = [
            'id',
            'name',
            'chapter',
            'quiz'
        ]

#contact page serializer
class ContactPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = contact_details
        fields = [
            'id',
            'name',
            'telephone',
            'telephone2',
            'whatsapp',
            'instagram',
            'twitter',
            'telegram',
            'discord',
            'facebook',
        ]

class ChapterSerializer(serializers.Serializer):
    name = serializers.CharField(read_only=True)

class ChapterListSerializer(serializers.ModelSerializer):
    #summary = serializers.HyperlinkedIdentityField(view_name='main:summary',lookup_field = 'slug',)

    class Meta:
        model = ChapterList
        fields = [
            'id',
            'course',
            'name',
            'slug',
            #'summary',
        ]

class SummaryPageSerializer(serializers.ModelSerializer):
    chapter = ChapterSerializer(read_only=True)
    class Meta:
        model = CourseSummary
        fields = [
            'id',
            'chapter',
            'body',
        ]

class QuizHomePageSerializer(serializers.ModelSerializer):
    #quiz = serializers.HyperlinkedIdentityField(view_name='quiz_list',lookup_field = "name")

    class Meta:
        model = CourseList
        fields = [
            'id',
            'name',
            #'quiz',
        ]

class CourseSerializer(serializers.Serializer):
    name = serializers.CharField(read_only=True)

class QuizListSerializer(serializers.ModelSerializer):
    course = ChapterSerializer(read_only=True)
    #quiz = serializers.HyperlinkedIdentityField(view_name='start_quiz',lookup_field = "id",)
    class Meta:
        model = Quiz
        fields = [
            'id',
            'course',
            'name',
            #'quiz',
        ]

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = [
            'choice',
            'correct',
        ]

class QuizSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(many=True, read_only=True)
    class Meta:
        model = Question
        fields = [
            'id',
            'question',
            'answer',
        ]