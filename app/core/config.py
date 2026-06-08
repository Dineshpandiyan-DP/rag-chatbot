from pydantic_settings import BaseSettings,SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    model_config=SettingsConfigDict(env_file=".env",
                                    env_file_encodings="utf-8",
                                    case_sesitive=False,
                                    extra="ignore")
    groq_api_key: str
    app_name:str= "CLARIX"
    embedding_model: str
    chroma_path: str="./chroma_db"
    chunk_size: int= 512
    port: int= 8000
    llm_mode: str= "llama-3.1-70b-versatile"
    environment: str= "development"
    app_vesion : str= "1.0.0"
     
@lru_cache()
def get_settings()-> Settings:
    return Settings()

print(get_settings())
