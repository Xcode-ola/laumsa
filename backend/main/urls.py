from django.urls import path, include
from .views import IndexPage, ContactPage, Chapters, SummaryPage, QuizHomePage, QuizListPage

urlpatterns = [
    path('', IndexPage.as_view(), name="index"),
    path('contacts/', ContactPage.as_view(), name="contacts"),
    path('course/<str:name>/', Chapters.as_view(), name="chapter"),
    path('course/<str:name>/<str:slug_field>/', SummaryPage.as_view(), name="summary"),
    path('quiz/', QuizHomePage.as_view(), name="quiz"),
    path('quiz/<str:name>/', QuizListPage.as_view(), name="quiz_list")
]