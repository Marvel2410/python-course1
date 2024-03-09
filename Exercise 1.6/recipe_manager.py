#STEP 1
import mysql.connector


#STEP 2 -  Initialize connection object
conn = mysql.connector.connect(
    host='localhost',
    user='cf-python',
    passwd='password'
)


#STEP3 - Inistialize a cursor object
cursor = conn.cursor()


#STEP 4 - reate a database "task_database"
cursor.execute("CREATE DATABASE IF NOT EXISTS task_database")


#STEP 5 - Access dtatabase with USE statement
cursor.execute("USE task_database")

#STEP 6 - Create the Table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Recipes (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(50),
        ingredients VARCHAR(255),
        cooking_time INT,
        difficulty VARCHAR(20)
    )
""")

def main_menu(conn, cursor):
    while True:
        print("\nMain Menu\n============================")
        print("Pick a choice:")
        print("\t1. Create a new recipe")
        print("\t2. Search for a recipe by ingredient")
        print("\t3. Update an existing recipe")
        print("\t4. Delete a recipe")
        print("\t5. View all recipes")
        print("\tType 'quit' to exit the program")
        choice = input("Your Choice: ")

        try:
            if choice == '1':
                create_recipe(conn, cursor)
            elif choice == '2':
                search_recipe(conn, cursor)
            elif choice == '3':
                update_recipe(conn, cursor)
            elif choice == '4':
                delete_recipe(conn, cursor)
            elif choice == '5':
                view_all_recipes(conn, cursor)
            elif choice.lower() == 'quit': #checks if user input is 'quit' and then ends program
                break
            else:  #if not quit, asks for a valid selection
                print("Invalid choice. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")




#calculating difficulty
def calculate_difficulty(cooking_time, ingredients):
    if cooking_time < 10 and len(ingredients) < 4:
        return 'Easy'
    elif cooking_time < 10 and len(ingredients) >= 4:
        return 'Medium'
    elif cooking_time >= 10 and len(ingredients) < 4:
        return 'Intermediate'
    elif cooking_time >= 10 and len(ingredients) >= 4:
        return 'Hard'


#creating a recipe
def create_recipe(conn, cursor):
    # Collect recipe details
    name = input("\nEnter the name of the recipe: ")
    cooking_time = int(input("Enter the cooking time (in minutes): "))
    ingredients = input("Enter ingredients (separated by commas): ").split(", ")

     

    # Calculate difficulty
    difficulty = calculate_difficulty(cooking_time, ingredients)

    # Convert ingredients list to a comma-separated string
    ingredients_str = ', '.join(ingredients)

    # Prepare SQL query to insert the recipe
    query = "INSERT INTO Recipes (name, ingredients, cooking_time, difficulty) VALUES (%s, %s, %s, %s)"
    values = (name, ingredients_str, cooking_time, difficulty)

    # Execute the query and commit changes
    cursor.execute(query, values)
    conn.commit()
    print("Recipe has been saved into database!")


def search_recipe(conn, cursor):
    # Retrieve list of ingredients
    cursor.execute("SELECT ingredients FROM Recipes")
    results = cursor.fetchall()

    # Extract unique ingredients
    all_ingredients = set()
    for row in results:
        ingredients = row[0].split(', ')
        all_ingredients.update(ingredients)

    # Display ingredient options
    print("\nAvailable Ingredients:")
    max_len = max(len(ingredient) for ingredient in all_ingredients)
    for i, ingredient in enumerate(all_ingredients, start=1):
        print(f"\t{i}. {ingredient}")

    # Prompt user to choose an ingredient
    ingredient_choice = int(input("\nEnter the number of the ingredient to search for: "))
    search_ingredient = list(all_ingredients)[ingredient_choice - 1]

    # Search for recipes
    query = "SELECT name, ingredients FROM Recipes WHERE ingredients LIKE %s"
    cursor.execute(query, ('%'+search_ingredient+'%',))
    search_results = cursor.fetchall()

    # Display search results
    print("\nSearch Results:")
    for result in search_results:
        name, ingredients = result
        print(f"{name}: {ingredients}")




#Part 5 - Updating a recipe
def update_recipe(conn, cursor):
    # Fetch all recipes and list them to the user
    cursor.execute("SELECT id, name FROM Recipes")
    results = cursor.fetchall()
    print("\nAll recipes:")
    print("ID\tName")
    print("--------------------")
    for row in results:
        print(f"{row[0]}\t{row[1]}")

    # Ask user for recipe ID to update
    recipe_id = input("\nEnter the ID of the recipe you want to update: ")

    # Ask user for the column to update
    print("\nChoose the column to update:")
    print("1. Name")
    print("2. Cooking Time")
    print("3. Ingredients")
    column_choice = input("Your Choice: ")

    # Collect the new value from the user
    new_value = input("\nEnter the new value: ")

    # Build and execute the query to update the recipe
    if column_choice == '1':
        query = "UPDATE Recipes SET name = %s WHERE id = %s"
        cursor.execute(query, (new_value, recipe_id))
    elif column_choice == '2':
        query = "UPDATE Recipes SET cooking_time = %s, difficulty = %s WHERE id = %s"
        cooking_time = int(new_value)
        cursor.execute(query, (cooking_time, calculate_difficulty(cooking_time, []), recipe_id))
    elif column_choice == '3':
        query = "UPDATE Recipes SET ingredients = %s, difficulty = %s WHERE id = %s"
        cursor.execute(query, (new_value, calculate_difficulty(0, new_value.split(', ')), recipe_id))
    else:
        print("Invalid choice. Please Try again.")


    conn.commit()
    print("Recipe has been updated!")

#part 6 - Deleting a Recipe
def delete_recipe(conn, cursor):
     # Fetch all recipes and list them to the user
    cursor.execute("SELECT id, name FROM Recipes")
    results = cursor.fetchall()
    print("\nAll recipes:")
    print("ID\tName")
    print("--------------------")
    for row in results:
        print(f"{row[0]}\t{row[1]}")

    # Ask user for recipe ID to delete
    recipe_id = input("\nEnter the ID of the recipe you want to delete: ")

    # Build and execute the query to delete the recipe
    query = "DELETE FROM Recipes WHERE id = %s"
    cursor.execute(query, (recipe_id,))

    conn.commit()
    print("Recipe has been deleted!")


#view all recipes in database
def view_all_recipes(conn, cursor):
    # Retrieve all recipes from the database
    cursor.execute("SELECT name, ingredients, cooking_time, difficulty FROM Recipes")
    all_recipes = cursor.fetchall()

    # Display all recipes
    print("\nAll Recipes:")
    for recipe in all_recipes:
        name, ingredients, cooking_time, difficulty = recipe
        print(f"Name: {name}")
        print(f"Ingredients: {ingredients}")
        print(f"Cooking Time: {cooking_time} minutes")
        print(f"Difficulty: {difficulty}")
        print("------------------------------------")



#Call the main_menu function
main_menu(conn, cursor)