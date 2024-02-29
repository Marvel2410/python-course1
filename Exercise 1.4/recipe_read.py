import pickle

with open('recipe_binary.bin', 'rb') as my_file:
    recipe = pickle.load(my_file)

print("Recipe details")
print("Name:  " + recipe['Name'])
print("Ingredients: " + ', '.join(recipe['Ingredients']))
print("Cooking Time: " + recipe['Cooking Time'])
print("Difficulty: " + recipe['Difficulty'])



