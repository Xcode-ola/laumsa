from django.urls import path, include
from .views import RegisterView, LoginView, UserView, LogoutView, UserProfileView

urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name="login"),
    path('profile/', UserView.as_view(), name="user"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('profile/edit/<int:pk>/', UserProfileView.as_view(), name="edit_profile"),
]