from django.urls import path
from videotoaudio.views import convert_to_audio

app_name = 'videotoaudio'

urlpatterns = [
    path('convert_to_audio/', convert_to_audio, name='convert_to_audio'),
]
