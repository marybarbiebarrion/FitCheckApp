import os
from openai import OpenAI

client = OpenAI(
    api_key="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",  # Use env var for security
    base_url="https://openrouter.ai/api/v1"
)

def ask_openrouter(food_name):
    prompt = f"Give a 1-sentence description of the food '{food_name}' in simple terms."
    messages = [{"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}]
    
    response = client.chat.completions.create(
        model="mistralai/mistral-7b-instruct",
        messages=messages
    )
    return response.choices[0].message.content.strip()
