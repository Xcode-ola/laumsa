from django.urls import path
from .views import IndexPage, ContactPage

urlpatterns = [
    path('', IndexPage.as_view(), name="index"),
    path('contacts/', ContactPage.as_view(), name="contacts"),
]