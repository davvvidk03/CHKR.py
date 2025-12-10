#Main Code Here

import os
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise RuntimeError("Time exceeded")

client = OpenAI(api_key=api_key)

# prompt = ("If I have some ground beef, rice and mushrooms, give me a simple and easy recipe and instructions for a couple internationally themed dishes using the ingredients I have.")

response = client.responses.create(
    model="gpt-4.1-mini",
    input=prompt,
)

def get_user_ingredients():
    while True:
        raw = input("Enter at least 3 ingredients you have available (separated by commas): ").strip()
        ingredients = [i.strip() for i in raw.split(,) if i.strip()]
        if len(ingredients) <= 3:
            return ingredients
        print ("You need to go shopping -- please enter 3 ingredients.\n")

def get_dietary_restriction():
    restriction = input("Please give any dietary restrctions -- vegan, Halal, diabetic-friendly etc: ")
    return restriction.strip()

def get_flavor_profile():
    profile = input(
        "Do you want a specific type of food? ie -- Asian, Mediterranean, Creole, Latin etc... if not, simply put 'no': ").strip()
    
    if profile.lower() in ["no", "none", "n", '']:
        return None
    return profile

def get_meal_type():
    meal = input("What type of meal is this? Breakfast, Lunch, Dinner or a snack?: ").strip()
    return meal



print(response.output_text)
