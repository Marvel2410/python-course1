recipes_list = []
ingredients_list = []


def take_recipe():
    name = input("Enter recipe name: ")
    cooking_time = int(input("Enter cooking time (in minutes): "))
    ingredients = [ingredient.strip() for ingredient in input("Enter ingredients (separated by a comma): ").split(",")]
    return {
        'name': name,
        'cooking_time': cooking_time,
        'ingredients': ingredients
    }


n = int(input("How many recipes would you like to enter?"))

for i in range(n):
    recipe = take_recipe()
    for ingredient in recipe['ingredients']:
        if ingredient not in ingredients_list:
            ingredients_list.append(ingredient)
    recipes_list.append(recipe)

for recipe in recipes_list:
    if recipe['cooking_time'] < 10 and len(recipe['ingredients']) < 4:
        difficulty = 'Easy'
    elif recipe['cooking_time'] < 10 and len(recipe['ingredients']) >= 4:
        difficulty = 'Medium'
    elif recipe['cooking_time'] >= 10 and len(recipe['ingredients']) < 4:
        difficulty = 'Intermediate'
    else:
        difficulty = 'Hard'

    print("\nRecipe: " + recipe['name'])
    print("Cooking Time: " + str(recipe['cooking_time']) + " minutes")
    print("Ingredients: " + ', '.join(recipe['ingredients']))
    print("Difficulty: " + difficulty + "\n")


def print_ingredients():
    ingredients_list.sort()
    print("\nAll Ingredients")
    print('______________')
    for ingredient in ingredients_list:
        print(ingredient)

print_ingredients()
