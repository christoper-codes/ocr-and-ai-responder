from rest_framework import serializers

class OCRFilesSerializer(serializers.Serializer):
    files = serializers.ListField(
        child=serializers.FileField(),
        allow_empty=False
    )

    def validate_files(self, value):
        for file in value:
            if file.content_type not in ['image/png', 'image/jpeg', 'application/pdf']:
                raise serializers.ValidationError(f"Unsupported file type: {file.content_type}")
        return value
