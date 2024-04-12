successful_recipes = []
missing_ingredients = []
substitution_check = False

HotHoneyChicken_ingredients = (
    ("chicken breasts", "hot honey", "buns", "pepperjack cheese"), 
    ("bacon", "butter", "salt", "pepper", "garlic powder", "paprika"), 
    {"pepperjack cheese":"cheese", "hot honey":"honey"},
    ("Hot Honey Chicken Sandwich")
)

MeatballSubs_ingredients = (
    ("meatballs", "garlic bread", "marinara sauce"),
    ("mozzarella cheese"),
    {},
    ("Meatball Garlic Bread Sub")
)

SmokedMacAndCheese_ingredients = (
    ("macaroni", "butter", "velveeta cheese", "colby jack cheese", "eggs", "milk"),
    ("pepper", "garlic powder", "dry mustard", "paprika"),
    {},
    ("Smoked Mac and Cheese")
)

ingredients_list = [HotHoneyChicken_ingredients, MeatballSubs_ingredients, SmokedMacAndCheese_ingredients]

def recipe_checker():
    global substitution_check
    n = 0
    for ingredient in recipe[0]:
        change = False
        if ingredient in available_ingredients:
            n += 1
            change = True
        if change == False:
            missing_ingredients.append(ingredient)
            substitution_check = substitution_checker()
            if substitution_check:
                n+=1
    if n == len(recipe[0]):
        n = 0
        percentage = optional_checker()
        successful_recipes.append((recipe[3], percentage, substitution_check))
        substitution_check = False


def optional_checker():
    n = 0
    for available in available_ingredients:
        if available in recipe[1]:
            n +=1
    return round(100 * n / len(recipe[1]),2)

def substitution_checker():
    substitution_keys = recipe[2].keys()
    for ingredient in missing_ingredients:
        if ingredient in substitution_keys:
            if recipe[2][ingredient] in available_ingredients:
                missing_ingredients.remove(ingredient)
    if missing_ingredients == []:
        return True
                
        

available_ingredients = input("Ingredients, for example (beef, eggs, milk):")
available_ingredients = available_ingredients.split(", ")

for recipe in ingredients_list:
    recipe_checker()

if len(successful_recipes) == 0:
    print("You can't make SHIT")
else:
    print(successful_recipes)