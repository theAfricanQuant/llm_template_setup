import dspy
from config import settings

def setup_dspy(model_name: str):
    lm = dspy.LM(
        model=f"openai/{model_name}",
        api_key=settings.OPENROUTER_API_KEY,
        api_base=settings.OPENROUTER_BASE_URL,
        cache=False # Set to True to save credits during development
    )
    dspy.configure(lm=lm)

# 1. Define a Signature (the task description)
class SimpleQA(dspy.Signature):
    """Answer a question briefly and casually."""
    question = dspy.InputField()
    answer = dspy.OutputField(desc="A short, one-sentence answer")

def main():
    # Test with Gemini Flash from your config
    print(f"--- Testing DSPy with {settings.GEMINI_FLASH} ---")
    setup_dspy(settings.GEMINI_FLASH)

    # 2. Define a Module (ChainOfThought adds reasoning steps automatically)
    qa_module = dspy.ChainOfThought(SimpleQA)

    # 3. Call the module
    question = "Why is the sky blue?"
    response = qa_module(question=question)

    print(f"Question: {question}")
    print(f"Reasoning: {response.reasoning}")
    print(f"Answer: {response.answer}")

if __name__ == "__main__":
    main()
