from utils.llm_utils import call_llm
from config import settings

def main():
    print("--- OpenRouter Multi-Model Test ---")
    
    # Define the list of models we want to test from our config
    models_to_test = [
        settings.GLM_4,
        settings.GEMINI_FLASH,
        settings.GEMINI_PRO,
        settings.GPT_4O
    ]
    
    prompt = "Give me a one-sentence fun fact about space."

    for model_id in models_to_test:
        print(f"\n[Testing Model: {model_id}]")
        response = call_llm(prompt, model=model_id)
        print(f"Response: {response}")
        print("-" * 30)

if __name__ == "__main__":
    main()