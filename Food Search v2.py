successful_recipes = []
recipe_dict = [
    {
        "name":"Hot Honey Chicken Sandwich",
        "required":("chicken breasts", "hot honey", "buns", "pepperjack cheese"), 
        "optional":("bacon", "butter", "salt", "pepper", "garlic powder", "paprika"),
        "substitutions":{"pepperjack cheese":"cheese", "hot honey":"honey"}
    },

    {
        "name":"Garlic Bread Meatball Sub",
        "required":("meatballs", "garlic bread", "marinara sauce"),
        "optional":("mozzarella",),
        "substitutions":{}
    },

    {
        "name":"Smoked Mac n Cheese",
        "required":("macaroni", "butter", "velveeta cheese", "colby jack cheese", "eggs", "milk"),
        "optional":("pepper", "garlic powder", "dry mustard", "paprika"),
        "substitutions":{}
    }
]

for recipe in recipe_dict:
    successful_recipes.append(recipe["name"])

def recipe_checker():
    percentage = 0
    for ingredient in recipe["optional"]:
        if ingredient in available_ingredients:
            percentage += 100/len(recipe["optional"])
    for ingredient in recipe["required"]:
        if ingredient not in available_ingredients and ingredient not in recipe["substitutions"]:
            successful_recipes.remove(recipe["name"])
        elif ingredient in available_ingredients:
            continue
        elif recipe["substitutions"][ingredient] in available_ingredients:
            continue
        else:
            successful_recipes.remove(recipe["name"])
        break


available_ingredients = input("Ingredients, for example (beef, eggs, milk):")
available_ingredients = available_ingredients.split(", ")

for recipe in recipe_dict:
    recipe_checker()

if len(successful_recipes) == 0:
    print("You can't make SHIT")
else:
    print("You can make " + str(successful_recipes))