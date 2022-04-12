from django.urls import path
from .views import Exist_API, Manage_API, Redirect_API, Sender_API

urlpatterns = [
    path('redirect/<str:sendBy>/<str:receiver>', Redirect_API.as_view()),
    path('sender/<str:sendBy>', Sender_API.as_view()),
    path('manage/<str:sender>/<str:receiver>/<str:sig>', Manage_API.as_view()),
    path('manage/<str:sender>/<str:receiver>/<str:sig>/<str:email>', Manage_API.as_view()),
    path('exist/<str:receiver>', Exist_API.as_view()),
]