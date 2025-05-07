import openai
client = openai.OpenAI(
    api_key="sk-1234",             # pass litellm proxy key, if you're using virtual keys or any random key
    base_url="http://localhost:4000" # litellm-proxy-base url
)

response = client.chat.completions.create(
    model="llama3",
    messages = [
        {
            "role": "user",
            "content": "what llm are you"
        }
    ],
)

print(response)