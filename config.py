from pydantic_settings import BaseSettings
from dotenv import load_dotenv
from typing import List

# Load environment variables from .env file
load_dotenv()


class Settings(BaseSettings):
    openai_api_key: str
   

    class Config:
        env_file = ".env"

settings = Settings()