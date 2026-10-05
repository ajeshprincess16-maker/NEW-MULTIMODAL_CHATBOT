class VisionService:
    def analyze_image(self, image_path: str, prompt: str):
        return f"Image analysis for {prompt}"

vision_service = VisionService()
