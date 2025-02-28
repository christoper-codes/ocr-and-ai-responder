class GeneratePromptAction:
    @staticmethod
    def execute(question: str, text: str) -> str:
        return f"hello, I need you to solve this question {question}, based on this text: {text}"
