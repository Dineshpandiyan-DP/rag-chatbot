from pydantic_settings import BaseSettings,SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    model_config=SettingsConfigDict(env_file=".env",
                                    env_file_encoding="utf-8",
                                    case_sensitive=False,
                                    extra="ignore")
    groq_api_key: str
    app_name: str= "CLARIX"
    embedding_model: str= "all-MiniLM-L6-v2" 
    chroma_path: str="./chroma_db"
    chunk_size: int= 512
    port: int= 8000
    llm_model: str= "llama-3.1-70b-versatile"
    environment: str= "development"
    app_version: str= "1.0.0"
     
@lru_cache()
def get_settings()-> Settings:
    return Settings()

print(get_settings())
