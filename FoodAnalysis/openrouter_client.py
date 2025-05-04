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
    
    description = response.choices[0].message.content.strip()
    return description

def ask_food_alternatives(food_name, ingredients, allergens):
    # prompt = (
    #     f"Suggest food alternatives for {food_name}, that is different from food itself, based on the following ingredients and allergens. "
    #     f"List alternatives that have almost similar ingredients but exclude the allergens listed.\n"
    #     f"Ingredients: {ingredients}\n"
    #     f"Allergens: {allergens}\n"
    #     f"Provide a list of alternatives with a short description and why each one is a good alternative."
    # )
    prompt = (
        f"Suggest 3 food alternatives for {food_name}, that is different from food itself, but lacks the allergens in the initial food. "
        f"Allergens: {allergens}\n"
        f"Provide a list of alternatives with a max-20-word explanation why each one is a good alternative."
    )
    
    messages = [{"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}]
    
    response = client.chat.completions.create(
        # model="mistralai/mistral-7b-instruct",
        model="openai/gpt-3.5-turbo",
        messages=messages
    )
    
    alternatives = response.choices[0].message.content.strip()
    
    formatted_alternatives = "\n\n".join(alternatives.split("\n"))
    
    return formatted_alternatives 