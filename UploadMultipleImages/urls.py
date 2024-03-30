from django.urls import path
from .views import ImageView
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('images/', ImageView.as_view(), name='images'),
    path('openapi/', get_schema_view(title="Images API"), name='openapi-schema'),
]
