import pickle

recipe = {
    'Name': 'Tea',
    'Ingredients': ['Tea Leaves', 'Water', 'Sugar'],
    'Cooking Time' : '5 minutes',
    'Difficulty': 'Easy'
}

my_file = open('recipe_binary.bin', 'wb')
pickle.dump(recipe, my_file)
my_file.close()