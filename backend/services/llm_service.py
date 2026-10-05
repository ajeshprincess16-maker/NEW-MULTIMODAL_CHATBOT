import os
from huggingface_hub import InferenceClient
from config import settings

class LLMService:
    def __init__(self):
        self.model_name = "Qwen/Qwen2.5-VL-3B-Instruct"
        self.client = InferenceClient(
            model=self.model_name,
            token=settings.HF_API_TOKEN
        )

    def generate_response(self, prompt: str, context: str = "", history: list = None):
        """
        Generate text response from the model.
        history is a list of dicts: [{"role": "user"|"assistant", "content": "..."}]
        """
        messages = []
        if context:
            messages.append({"role": "system", "content": f"Context: {context}"})
            
        if history:
            messages.extend(history)
            
        messages.append({"role": "user", "content": prompt})

        try:
            response = self.client.chat_completion(
                messages=messages,
                max_tokens=1024,
                temperature=0.7,
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"LLM Error: {e}")
            return f"Error connecting to AI service. Please check your HF_API_TOKEN or model status."

llm_service = LLMService()
