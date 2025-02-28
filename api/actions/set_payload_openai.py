class SetPayloadOpenAIAction:
    @staticmethod
    def execute(model: str, prompt: str) -> dict:
        return {
            'model': model,
            'messages': [
                {'role': 'user', 'content': prompt}
            ],
        }
