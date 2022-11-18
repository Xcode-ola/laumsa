from rest_framework import serializers
from .models import CourseList, Quiz, contact_details, ChapterList, CourseSummary

#homepage serializer for the website. The page contains all the courses and a link to the contact address
class IndexPageSerializer(serializers.ModelSerializer):
    chapter = serializers.HyperlinkedIdentityField(
        view_name='chapter',
        lookup_field = "name"
    )
    class Meta:
        model = CourseList
        fields = [
            'id',
            'name',
            'chapter',
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

class ChapterListSerializer(serializers.ModelSerializer):
    summary = serializers.HyperlinkedIdentityField(
        view_name='summary',
        lookup_field = "slug"
    )

    class Meta:
        model = ChapterList
        fields = [
            'id',
            'course',
            'name',
            'slug',
            'summary',
        ]

class ChapterSerializer(serializers.Serializer):
    name = serializers.CharField(read_only=True)

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
    quiz = serializers.HyperlinkedIdentityField(
        view_name='quiz_list',
        lookup_field = "name"
    )

    class Meta:
        model = CourseList
        fields = [
            'id',
            'name',
            'quiz',
        ]

class CourseSerializer(serializers.Serializer):
    name = serializers.CharField(read_only=True)

class QuizListSerializer(serializers.ModelSerializer):
    course = ChapterSerializer(read_only=True)
    quiz = serializers.HyperlinkedIdentityField(
        view_name='quiz_list',
        lookup_field = "name"
    )
    class Meta:
        model = Quiz
        fields = [
            'id',
            'course',
            'name',
            'quiz',
        ]