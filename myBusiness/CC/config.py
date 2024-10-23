import os

# Ensure you set your OpenAI API key as an environment variable
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("Please set the 'OPENAI_API_KEY' environment variable")
