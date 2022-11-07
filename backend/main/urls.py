from django.urls import path, include
from .views import IndexPage, ContactPage, Chapters, SummaryPage
from .routers import urlpatterns

urlpatterns = [
    path('', IndexPage.as_view(), name="index"),
    path('contacts/', ContactPage.as_view(), name="contacts"),
    path('<str:name>/', Chapters.as_view(), name="chapter"),
    #path('', include(urlpatterns))
    path('<str:name>/<str:slug_field>/', SummaryPage.as_view(), name="summary")
]