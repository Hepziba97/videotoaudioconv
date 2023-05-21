from django.urls import path
from .views import convert_to_audio

urlpatterns = [
    path('convert_to_audio/', convert_to_audio, name='convert_to_audio'),
]
