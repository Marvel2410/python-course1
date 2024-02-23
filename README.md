Exercise 1.1
1.  Install python (make sure its 3.8.7)
2.  Create a virtual environment called "cf-python-base" with the following command: python -m venv cf-python-base
3.  Install VS Code (if haven't already)
4.  Create a Python script named "add.py" that adds two numbers. 
    - Use the input() function to get user input and the print() function to display the result.
5.  Activate the virtual environment with the following code and install pip: source cf-python-base/bin/activate
                                                                              pip install ipython
6.  Export a requirements file with the following command: pip freeze > requirements.txt
7.  Create a new environment named "cf-python-copy" and install packages from "requirements.txt" with:
          python -m venv cf-python-copy
          source cf-python-copy/bin/activate
          pip install -r requirements.txt
8. Create GitHub Repo and Document work



Exercise 1.2
  1.  Decide what data structure you would use for this purpose
      I'd use a dictionary for each recipe because it lets me store different details (name, ingredients, etc)
      using easy to use/remember names.  Especially for something like recipes, its easier for me to look at 
      it like having separate boxes for each recipe with labels on them.  I'd also use a list to keep all these 
      recipe boxes together in one place.  This will also allow me to easily add more recipes to my collection

  3. Figure out what type of structure you would consider for all_recipes, and briefly note down your justification in the README file. Ideally, this outer structure should be sequential in nature, where multiple recipes can be stored and modified as required.
    Lists are the best option becasue they will easily maintain order of the recipes.  It will allow me to store multiple recipes and allow for easy addition and modification. Using a list will keep it organized and make it eas to update, add or delete as needed.
      
      
 

