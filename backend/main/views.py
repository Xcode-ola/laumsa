from django.shortcuts import render
from .serializer import ContactPageSerializer, IndexPageSerializer
from .models import contact_details, CourseList
from rest_framework import generics, permissions

# Create your views here.
class IndexPage(generics.ListCreateAPIView):
    queryset = CourseList.objects.all()
    serializer_class = IndexPageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ContactPage(generics.ListCreateAPIView):
    queryset = contact_details.objects.all()
    serializer_class = ContactPageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
