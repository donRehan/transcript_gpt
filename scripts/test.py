import os
from dotenv import load_dotenv
import openai

openai_api_key = os.environ.get('OPENAI_API_KEY')
print(openai.Model.list())
