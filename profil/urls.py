from django.urls import path, include
from profil.views import UserProfileView


urlpatterns = [
    path('profile', UserProfileView.as_view()),
    ]