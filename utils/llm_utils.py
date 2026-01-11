from openai import OpenAI
from config import settings

client = OpenAI(
    base_url=settings.OPENROUTER_BASE_URL,
    api_key=settings.OPENROUTER_API_KEY,
)

def call_llm(prompt, model=settings.DEFAULT_MODEL):
    """
    Sends a prompt to the LLM. 
    Uses the provided model name, or defaults to the config setting.
    """
    try:
        completion = client.chat.completions.create(
            extra_headers={
                "HTTP-Referer": settings.SITE_URL, 
                "X-Title": settings.SITE_NAME,
            },
            model=model,
            messages=[
                {"role": "user", "content": prompt},
            ],
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Error with model {model}: {e}"