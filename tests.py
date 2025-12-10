
def get_user_ingredients():
    while True:
        raw = input("Enter at least 3 ingredients you have available (separated by commas): ").strip()
        # split on a comma string (not a bare comma token)
        ingredients = [i.strip() for i in raw.split(',') if i.strip()]
        # require at least 3 ingredients before returning
        if len(ingredients) >= 3:
            return ingredients
        reply = "You need to go shopping -- please enter 3 ingredients.\n"
        print(reply)
        return reply

get_user_ingredients()
