from django.urls import path
from .views import Banner_API

urlpatterns = [
    path('banner/<str:sendBy>/<str:receiver>', Banner_API.as_view()),
]