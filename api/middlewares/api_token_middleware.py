import os
from django.http import JsonResponse
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class APITokenMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        expected_token = os.getenv('API_TOKEN')
        api_token = request.GET.get('api_token')

        if api_token != expected_token:
            return JsonResponse({'error': 'Invalid API token'}, status=401)

        response = self.get_response(request)
        return response
