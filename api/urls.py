# api/urls.py

from django.urls import path
from .views.ocr_and_ai_responder import OCRAndAIResponder

urlpatterns = [
    path('ocr-ai-responder/', OCRAndAIResponder.as_view(), name='generate-video'),
]