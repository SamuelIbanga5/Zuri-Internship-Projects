from django.urls import path
from .views import *

urlpatterns = [
    path("data", DataAPIView.as_view()),
    path("data/<int:pk>/", GetDataAPIView.as_view())
]
