import pickle

def take_recipe():
    recipe_name = input("Enter recipe name: ")
    cooking_time = int(input("Enter cooking time (in minutes): "))
    ingredients = input("Enter ingredients (separated by commas): ").split(", ")
    difficulty = calc_difficulty(cooking_time, len(ingredients))
    return {'name': recipe_name, 'cooking_time': cooking_time, 'ingredients': ingredients, 'difficulty': difficulty}

def calc_difficulty(cooking_time, num_ingredients):
    if cooking_time < 10 and num_ingredients < 4:
        return 'Easy'
    elif cooking_time < 10 and num_ingredients >= 4:
        return 'Medium'
    elif cooking_time >= 10 and num_ingredients < 4:
        return 'Intermediate'
    else:
        return 'Hard'
    
filename = input("Enter filename to save to: ")
try:
    file = open(filename, 'rb')
    data = pickle.load(file)
    print("File loaded successfully!")
except FileNotFoundError:
    print("File doesn't exist, create a new file.")
    data = {"recipes_list": [], "all_ingredients": []}
except:
    print("An unexpected error occurred, try again.")
    data = {"recipes_list": [], "all_ingredients": []}
else:
    file.close()
finally:
   recipes_list = data["recipes_list"]
   ingredient_list = data["all_ingredients"]


n = int(input("How many recipes would you like to enter?"))

recipes_list = data.get('recipes_list', [])
ingredients_list = data.get('all_ingredients', [])

for i in range(n):
    recipe = take_recipe()
    for ingredient in recipe['ingredients']:
        if ingredient not in ingredients_list:
            ingredients_list.append(ingredient)
    recipes_list.append(recipe)
    print("Recipe added successfully!")

data['recipes_list'] = recipes_list
data['all_ingredients'] = ingredients_list

updated_file = open(filename, "wb")
pickle.dump(data, updated_file)

updated_file.close()
print("Recipe file has been updated!")
