import os
from openai import OpenAI

client = OpenAI(
    api_key="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",  # Use env var for security
    base_url="https://openrouter.ai/api/v1"
)

def ask_food_description(food_name):
    prompt = f"Give a 1-sentence description of the food '{food_name}' in simple terms."
    messages = [{"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}]
    
    response = client.chat.completions.create(
        model="mistralai/mistral-7b-instruct",
        messages=messages
    )
    return response.choices[0].message.content.strip()

def ask_food_alternatives(food_name, ingredients, allergens):
    prompt = (
        f"Suggest food alternatives for {food_name} based on the following ingredients and allergens. "
        f"List alternatives that have almost similar ingredients but exclude the allergens listed.\n"
        f"Ingredients: {ingredients}\n"
        f"Allergens: {allergens}\n"
        f"Provide a list of alternatives with a short description and why each one is a good alternative."
    )
    
    messages = [{"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}]
    
    response = client.chat.completions.create(
        # model="mistralai/mistral-7b-instruct",
        model="openai/gpt-3.5-turbo",
        messages=messages
    )
    
    return response.choices[0].message.content.strip()