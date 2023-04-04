from django.urls import path
from .views import (
    hi,
    addition,
    subtraction,
    multiplication,
    division,
)

urlpatterns = [
    path('hi', hi),
    path('addition', addition),
    path('subtraction', subtraction),
    path('multiplication', multiplication),
    path('division', division),
]
