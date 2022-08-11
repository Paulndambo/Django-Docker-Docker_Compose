from django.urls import path
from .import views

urlpatterns = [
    path("", views.EmailSendAPIView.as_view(), name="emails"),
]