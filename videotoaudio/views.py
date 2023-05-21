from django.shortcuts import render
from django.http import HttpResponse
from moviepy.editor import *

def convert_to_audio(request):
    if request.method == 'POST':
        # Get the video file from the request
        video_file = request.FILES['video_file']

        # Open the video file using moviepy
        video_clip = VideoFileClip(video_file.temporary_file_path())

        # Extract the audio from the video
        audio_clip = video_clip.audio

        # Set the output file name and path
        output_file = 'output.mp3'

        # Save the audio clip as an mp3 file
        audio_clip.write_audiofile(output_file)

        # Close the video and audio clips
        video_clip.close()
        audio_clip.close()

        # Return the audio file to the user
        with open(output_file, 'rb') as f:
            response = HttpResponse(f.read(), content_type='audio/mpeg')
            response['Content-Disposition'] = 'attachment; filename=output.mp3'
            return response

    # If the request method is not POST, render the template with a form for uploading the video file
    return render(request, 'convert_to_audio.html')
