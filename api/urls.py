from django.urls import path
from .views import (
    HiView,
    addition,
    subtraction,
    multiplication,
    division,
)

urlpatterns = [
    path('hi', HiView.as_view()),
    path('addition', addition),
    path('subtraction', subtraction),
    path('multiplication', multiplication),
    path('division', division),
]
