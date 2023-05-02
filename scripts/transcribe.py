import os
from dotenv import load_dotenv
import sys
import openai

openai_api_key = os.environ.get('OPENAI_API_KEY')
video_url = sys.argv[1]
audio_file_path = os.path.join(os.getcwd(), 'tmp', video_url + '.m4a')

audio_file = open(audio_file_path, 'rb')
transcript = openai.Audio.transcribe(
    file=audio_file,
    model="whisper-1",
    response_format="srt",
    prompt="I am alhussien Rehan and this is an application for the OpenAI api practice for skills. I am going to transcribe this audio file.",
)
