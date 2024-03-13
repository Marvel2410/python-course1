#Define class recipe
class Recipe:
  def __init__(self, name, ingredients=[], cooking_time=0):
      self.name = name
      self.ingredients = ingredients
      self.cooking_time = cooking_time
      self.difficulty = self.calc_difficulty()


#method to add ingredients to the recipe
  def add_ingredients(self, *ingredients):
      self.ingredients.extend(ingredients)
      self.update_all_ingredients()

#method to update ingredients
  def update_all_ingredients(self):
      for ingredient in self.ingredients:
          if ingredient not in Recipe.all_ingredients:
              Recipe.all_ingredients.append(ingredient)

#method to calculate difficulty of recipe based off cooking time and ingredients
  def calc_difficulty(self):
      if self.cooking_time < 10 and len(self.ingredients) < 4:
          return "Easy" 
      elif self.cooking_time < 10 and len(self.ingredients) >= 4:
          return "Medium"
      elif self.cooking_time >= 10 and len(self.ingredients) < 4:
          return "Intermediate"
      elif self.cooking_time >= 10 and len(self.ingredients) >= 4:
          return "Hard"

#method to serach for a specific ingredient
  def search_ingredient(self, ingredient):
          return ingredient in self.ingredients
  
#method to return a string represenation of the recipe
  def __str__(self):
      return f"Recipe: {self.name}\nIngredients: {', '.join(self.ingredients)}\nCooking Time: {self.cooking_time} minutes\nDifficulty: {self.difficulty}"
  

#define a class variable to keep track of all ingredients within all recipes
Recipe.all_ingredients = []

#search for recipes contianing a specific ingredient
def recipe_search(data, search_term):
    for recipe in data:
        if recipe.search_ingredient(search_term):
            print(recipe)

# Create recipe objects
tea = Recipe("Tea", ["Tea Leaves", "Sugar", "Water"], 5)
coffee = Recipe("Coffee", ["Coffee Powder", "Sugar", "Water"], 5)
cake = Recipe("Cake", ["Sugar", "Butter", "Eggs", "Vanilla Essence", "Flour", "Baking Powder", "Milk"], 50)
banana_smoothie = Recipe("Banana Smoothie", ["Bananas", "Milk", "Peanut Butter", "Sugar", "Ice Cubes"], 5)

#display string representation of recipe objects
print(tea)
print(coffee)
print(cake)
print(banana_smoothie)

#wrapping recipes into recipes_list
recipes_list = [tea, coffee, cake, banana_smoothie]

#search for recipes containing specific ingredients
print("\nRecipes with 'Water':")
recipe_search(recipes_list, "Water")
print("\nRecipes with 'Sugar':")
recipe_search(recipes_list, "Sugar")
print("\nRecipes with 'Bananas':")
recipe_search(recipes_list, "Bananas")