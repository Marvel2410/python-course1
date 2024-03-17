from django.db import models

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    cooking_time = models.IntegerField()
    ingredients = models.TextField()
    difficulty_level_choices = (
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    )
    difficulty_level = models.CharField(max_length=10, choices=difficulty_level_choices)

    
    def __str__(self):
        return self.name
