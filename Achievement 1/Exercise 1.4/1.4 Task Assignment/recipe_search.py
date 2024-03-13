import pickle

# function to display a recipe's details
def display_recipe(recipe):
    print("Recipe Name:", recipe['name'])
    print("Cooking Time:", recipe['cooking_time'], "minutes")
    print("Ingredients:", ", ".join(recipe['ingredients']))
    print("Difficulty:", recipe['difficulty'])


# function to search for a specific ingredients in recipes
def search_ingredient(data):
    while True:
        try:
            # Display available ingredients to choose from
            print("Available Ingredients:")
            for idx, ingredient in enumerate(data['all_ingredients'], start=1):
                print(f"{idx}. {ingredient}")

            # Prompt user to select an ingredient by number
            ingredient_idx = int(input("Enter the number corresponding to the ingredient you want to search for: "))
            if 1 <= ingredient_idx <= len(data['all_ingredients']):
                # Get the selected ingredient
                ingredient_searched = data['all_ingredients'][ingredient_idx - 1]
                print(f"Recipes containing '{ingredient_searched}':")
                found_recipes = False
                # Check each recipe for the selected ingredient and display matching recipes
                for recipe in data['recipes_list']:
                    if ingredient_searched in recipe['ingredients']:
                        display_recipe(recipe)
                        found_recipes = True
                if not found_recipes:
                    print("No recipes found containing this ingredient.")
            elif ingredient_idx == 0: #Exit out option
                break
            else:
                print("Invalid input, try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Main code to load recipe data and search for recipes by ingredient
filename = input("Enter the filename that contains your recipe data: ")
try:
    with open(filename, 'rb') as file:
        data = pickle.load(file)  # Load recipe data from the file
        search_ingredient(data)   # Call the search_ingredient function with the loaded data
except FileNotFoundError:
    print("File not found.")