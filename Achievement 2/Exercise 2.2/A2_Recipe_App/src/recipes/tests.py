from django.test import TestCase
from .models import Recipe

# Create your tests here.
class RecipeModelTest(TestCase):
    
    def test_recipe_name(self):
        recipe = Recipe.objects.create(name='Pancakes', description='Delicious pancakes recipe', cooking_time=30, ingredients='Flour, eggs, milk', difficulty_level='easy')
        expected_name = recipe.name
        self.assertEqual(expected_name, 'Pancakes')

    def test_cooking_time(self):
        recipe = Recipe.objects.create(name='Pancakes', description='Delicious pancakes recipe', cooking_time=30, ingredients='Flour, eggs, milk', difficulty_level='easy')
        self.assertEqual(recipe.cooking_time, 30)

    def test_difficulty_level(self):
        recipe = Recipe.objects.create(name='Pancakes', description='Delicious pancakes recipe', cooking_time=30, ingredients='Flour, eggs, milk', difficulty_level='hard')
        self.assertEqual(recipe.difficulty_level, 'hard')

    def test_name_max_length(self):
        max_length = Recipe._meta.get_field('name').max_length
        self.assertEqual(max_length, 100)