from django.urls import path
from . import views

urlpatterns = [
    path('<str:address>/', views.metadata),
]