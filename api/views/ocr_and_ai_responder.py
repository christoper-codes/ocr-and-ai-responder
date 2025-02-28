from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.serializers import OCRFilesSerializer  
from api.actions.extract_text_from_image import ExtractTextFromImage
from api.actions.extract_text_from_pdf import ExtractTextFromPDF
from api.actions.set_payload_openai import SetPayloadOpenAIAction
from api.actions.openai_text_api import OpenAITextApi
from api.actions.generate_prompt import GeneratePromptAction
import pytesseract

# route to tesseract.exe
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

class OCRAndAIResponder(APIView):
    def get(self, request):
        try:
            # Validate the request data
            serializer = OCRFilesSerializer(data=request.data)
            if serializer.is_valid():
                files = serializer.validated_data['files']  
                question = request.data.get('question')
                result = []

                for file in files:
                    if file.content_type in ['image/png', 'image/jpeg']:
                        text = ExtractTextFromImage.execute(file)
                    elif file.content_type == 'application/pdf':
                        text = ExtractTextFromPDF.execute(file)                        
                    result.append({'filename': file.name, 'text': text})

                combined_text = " ".join([res['text'] for res in result])
                prompt = GeneratePromptAction.execute(question, combined_text)

                payload = SetPayloadOpenAIAction.execute('gpt-4o-mini', prompt)
                response = OpenAITextApi.generate_text_content(payload)
                
                return Response(response['response'], status=status.HTTP_200_OK)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)