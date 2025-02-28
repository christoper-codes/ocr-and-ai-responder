import os
import json
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class OpenAITextApi:
    @staticmethod
    def generate_text_content(payload: dict) -> dict:
        endpoint = 'https://api.openai.com/v1/chat/completions'
        api_key = os.getenv('API_KEY_OPENAI')

        response = requests.post(
            endpoint,
            headers={
                'Authorization': f'Bearer {api_key}',
                'Content-Type': 'application/json',
            },
            json=payload
        )

        if response.status_code == 200:
            try:
                content = response.json().get('choices')[0]['message']['content']
                clean_content = " ".join(content.split())
                return {'response': clean_content}
            except (ValueError, KeyError, IndexError) as e:
                return {'error': f'Error parsing response: {str(e)}'}
        else:
            return {'error': f'Error from API: {response.status_code} {response.text}'}
