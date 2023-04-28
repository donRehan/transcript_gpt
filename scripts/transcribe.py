import os
from dotenv import load_dotenv
import sys
import openai

openai_api_key = os.environ.get('OPENAI_API_KEY')
video_url = sys.argv[1]
audio_file = os.path.join(os.getcwd(), 'tmp', video_url + '.m4a')
print(audio_file)
