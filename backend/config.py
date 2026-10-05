from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://postgres:postgres@localhost:5432/chatbot"
    HF_API_TOKEN: str = ""
    EMBEDDING_API_KEY: str = ""
    WEB_SEARCH_API_KEY: str = ""

    class Config:
        env_file = ".env"

settings = Settings()
