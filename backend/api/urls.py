from django.urls import path
from .views import Redirect_API, Sender_API

urlpatterns = [
    path('redirect/<str:sendBy>/<str:receiver>', Redirect_API.as_view()),
    path('sender/<str:sendBy>', Sender_API.as_view()),
]