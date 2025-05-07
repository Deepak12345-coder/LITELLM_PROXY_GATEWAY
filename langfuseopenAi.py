import os
from langfuse.openai import openai

# Configure Langfuse & OpenAI Environment in .env file
# Set Langfuse API keys from your Langfuse project
os.environ["LANGFUSE_PUBLIC_KEY"] = "pk-1234"
os.environ["LANGFUSE_SECRET_KEY"] = "sk-1234"
os.environ["LANGFUSE_HOST"] = "http://localhost:3000"  # or US if applicable

os.environ["OPENAI_API_KEY"] = "sk-your-openai-key"

# Set your LiteLLM Proxy URL
PROXY_URL = "http://localhost:4000"

# Init OpenAI client to use LiteLLM proxy
client = openai.OpenAI(base_url=PROXY_URL)

# SYSTEM PROMPT
system_prompt = "You are a very accurate calculator. You output only the result of the calculation."

# 🔷 Test with OpenAI GPT-3.5-Turbo

# 🔶 Test with Ollama LLaMA3
llama_completion = client.chat.completions.create(
    model="ollama/llama3",
    name="llama3",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": "3 + 3 = "}
    ]
)
print("LLaMA3 Response:", llama_completion.choices[0].message.content)