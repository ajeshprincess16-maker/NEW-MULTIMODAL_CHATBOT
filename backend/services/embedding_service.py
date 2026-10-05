class EmbeddingService:
    def generate_embeddings(self, text: str):
        return [0.0] * 1536 # Mock embedding

embedding_service = EmbeddingService()
