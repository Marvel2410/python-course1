#Import necessary packages
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#Extra borders/animations fun
import os
import time

#Set up SQLAlchemy
username = "cf-python"
password = "password"
hostname = "localhost"
database_name = "task_database"

#Create engine object
engine = create_engine(f"mysql://{username}:{password}@{hostname}/{database_name}")

#Create Base object
Base = declarative_base()

#Generate Session class and initialize session object
Session = sessionmaker(bind=engine)
session = Session()

#Define recipe model
class Recipe(Base):
  #Set the table's name as final_recipes
  __tablename__ = 'final_recipes'

  #Define columns for the table
  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String(50)) #Recipe name with max lenth of 50 characters
  ingredients = Column(String(255)) #Ingredients with max lenth of 255 characters
  cooking_time = Column(Integer) #Cooking time in minutes
  difficulty = Column(String(20)) #Difficulty level, string with max length of 20 characters

  #Define the __repr__ method to show a quick representation of the recipe
  def __repr__(self):
      return f"<Recipe ID: {self.id}, Name: {self.name}, Difficulty: {self.difficulty}>"
  
  #Define the __str__ method to print a well-formatted version of the recipe
  def __str__(self):
      return f"Recipe: {self.name}\nCooking Time: {self.cooking_time} minutes\nDifficulty: {self.difficulty}\nIngredients: {self.ingredients}"
  
  # Define a method to calculate the difficulty of a recipe based on the number of ingredients and cooking time
  def calculate_difficulty(self):
      num_ingredients = len(self.ingredients.split(', '))
      if self.cooking_time <= 10 and num_ingredients <= 5:
          self.difficulty = 'Easy'
      elif self.cooking_time <= 30 and num_ingredients <= 10:
          self.difficulty = 'Medium'
      elif self.cooking_time <= 60 and num_ingredients <= 15:
          self.difficulty = 'Intermediate'
      else:
          self.difficulty = 'Hard'

  # Define a method to retrieve the ingredients string inside the Recipe object as a list
  def return_ingredients_as_list(self):
      if self.ingredients == '':
          return []
      else:
          return self.ingredients.split(', ')

# Create the corresponding table on the database
Base.metadata.create_all(engine)


# Function to display a border
def display_border(length):
    print("+" + "-"*length + "+")

# Function to display a menu option with a border
def display_menu_option(number, option, length):
    print(f"| {number}. {option.ljust(length-5)} |")

# Function to animate text
def animate_text(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()





#Function to create a new recipe entry
def create_recipe():
    display_border()
    print("|       Create a new recipe       |")
    display_border()
    # Collect recipe details
    name = input("\nEnter the name of the recipe: ")
    ingredients = input("Enter ingredients (separated by commas): ").split(", ")
    cooking_time = input("Enter the cooking time (in minutes): ")

    try:
        cooking_time = int(cooking_time)
    except ValueError:
        print("Invalid input. Please enter a valid number for cooking time.")
        return

    # Validate inputs
    if len(name) > 50:
        print("Recipe name must be 50 characters or less. Please try again.")
        return
    
    # Join the list of ingredients into a string
    ingredients_str = ", ".join(ingredients)

    # Create Recipe object
    new_recipe = Recipe(name=name, ingredients=ingredients_str, cooking_time=cooking_time)

    # Calculate difficulty
    new_recipe.calculate_difficulty()

    # Add new recipe to database
    session.add(new_recipe)
    session.commit()

    print("Recipe has been added")
    
#Retrieve all recipes from the database
def view_all_recipes():
    recipes = session.query(Recipe).all()

    if not recipes:
        print("No recipes found.")
    else:
        for recipe in recipes:
            print(recipe)

#Check if there are any recipes in the database
def search_by_ingredients():
    if session.query(Recipe).count() == 0:
        print("No recipes found.")
        return

    #=Retrieve all ingredients from the database
    results = session.query(Recipe.ingredients).all()
    all_ingredients = set()
    for result in results:
        ingredients = result[0].split(", ")
        for ingredient in ingredients:
            all_ingredients.add(ingredient)

    # Display all available ingredients
    print("Available ingredients:")
    for i, ingredient in enumerate(all_ingredients, 1):
        print(f"{i}. {ingredient}")

    #Ask the user to input ingredient numbers, separated by spaces
    user_input = input("Enter ingredient numbers separated by spaces: ")
    selected_ingredients = []
    for num in user_input.split():
        if not num.isdigit() or int(num) < 1 or int(num) > len(all_ingredients):
            print("Invalid input. Please try again.")
            return
        selected_ingredients.append(list(all_ingredients)[int(num) - 1])


    # Build search conditions for selected ingredients
    conditions = []
    for ingredient in selected_ingredients:
        conditions.append(Recipe.ingredients.like(f"%{ingredient}%"))

    # Retrieve recipes
    recipes = session.query(Recipe).filter(*conditions).all()

    # Display matching recipes
    for recipe in recipes:
        print(recipe)


#Edit recipes
def edit_recipe():
    #Check if there are any recipes in the database

    if session.query(Recipe).count() == 0:
        print("No recipes found.")
        return

    # Retrieve recipe details
    results = session.query(Recipe.id, Recipe.name).all()

    # Display recipes
    for result in results:
        print(f"{result.id}. {result.name}")

    # User selects recipe
    recipe_id = int(input("Enter recipe ID to edit: "))

    # Retrieve recipe to edit
    recipe_to_edit = session.query(Recipe).get(recipe_id)

    # Display recipe details
    print(f"Editing recipe: {recipe_to_edit.name}")
    print("1. Name\n2. Ingredients\n3. Cooking Time")
    attribute = int(input("Select attribute to edit: "))

    # Edit selected attribute of the recipe
    if attribute == 1:
        new_name = input("Enter new name: ")
        recipe_to_edit.name = new_name
    elif attribute == 2:
        new_ingredients = input("Enter new ingredients separated by commas: ")
        recipe_to_edit.ingredients = new_ingredients
    elif attribute == 3:
        new_cooking_time = input("Enter new cooking time in minutes: ")
        recipe_to_edit.cooking_time = int(new_cooking_time)
    
    #Recalculate difficulty
    recipe_to_edit.calculate_difficulty()

    #Commit changes
    session.commit()

#Delete/Remove recipes
def delete_recipe():
    # Check for entries
    if session.query(Recipe).count() == 0:
        print("No recipes found.")
        return

    # Retrieve recipe details
    results = session.query(Recipe.id, Recipe.name).all()

    # Display recipes
    for result in results:
        print(f"{result.id}. {result.name}")

    # User selects recipe
    recipe_id = int(input("Enter recipe ID to delete: "))

    # Retrieve recipe to delete
    recipe_to_delete = session.query(Recipe).get(recipe_id)

    # Confirm deletion
    confirm = input(f"Are you sure you want to delete {recipe_to_delete.name}? (yes/no): ")
    if confirm.lower() == "yes":
        session.delete(recipe_to_delete)
        session.commit()


#Creating the main menu
def main_menu():
    options = [
        "Create a new recipe",
        "View all recipes",
        "Search for recipes by ingredients",
        "Edit a recipe",
        "Delete a recipe",
        "Quit"
    ]
    max_length = max(len(option) for option in options) + 6  # Add 6 for padding and numbering

    while True:
        display_border(max_length)
        print("|              Recipe App               |")
        display_border(max_length)
        print("| Main Menu:                            |")
        for i, option in enumerate(options, 1):
            display_menu_option(i, option, max_length)
        display_border(max_length)

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
          create_recipe()
        elif choice == "2":
            view_all_recipes()
        elif choice == "3":
            search_by_ingredients()
        elif choice == "4":
            edit_recipe()
        elif choice == "5":
            delete_recipe()
        elif choice == "6" or choice.lower() == "quit":
            print("You have exited the application, Goodbye!")
            session.close()
            engine.dispose()
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main menu
if __name__ == "__main__":
    main_menu()