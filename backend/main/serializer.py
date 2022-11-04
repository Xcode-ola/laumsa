from rest_framework import serializers
from .models import CourseList, contact_details, ChapterList, CourseSummary

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
        lookup_field = "slug",
        #lookup_field = "course",
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

class SummaryPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseSummary
        fields = [
            'id',
            'chapter',
            'body',
        ]