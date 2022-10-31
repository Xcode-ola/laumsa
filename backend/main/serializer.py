from rest_framework import serializers
from .models import CourseList, contact_details

#homepage serializer for the website. The page contains all the courses and a link to the contact address
class IndexPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseList
        fields = [
            'id',
            'name',
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