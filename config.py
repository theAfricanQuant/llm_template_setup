from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # API Configuration
    # Pydantic will automatically look for OPENROUTER_API_KEY in the .env file
    OPENROUTER_API_KEY: str
    OPENROUTER_BASE_URL: str = "https://openrouter.ai/api/v1"
    SITE_URL: str = "http://localhost:3000"
    SITE_NAME: str = "LLM Project"

    # Model Identifiers
    GLM_4: str = "z-ai/glm-4.7"
    GEMINI_FLASH: str = "google/gemini-3-flash-preview"
    GEMINI_PRO: str = "google/gemini-3-pro-preview"
    GPT_4O: str = "openai/gpt-4o"
    
    # Default model selection
    DEFAULT_MODEL: str = "google/gemini-3-flash-preview"

    # Configuration for Pydantic to load from .env
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

# Instantiate the settings object
settings = Settings()
