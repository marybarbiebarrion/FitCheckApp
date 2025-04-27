from django.db import models

# Create your models here.
class Ingredient(models.Model):
    ingredient_id = models.AutoField(primary_key=True)
    ingredient_name = models.CharField(max_length=256, null=False)  
    
    def __str__(self):
        return self.ingredient_name 

class Recipe(models.Model):
    recipe_id = models.AutoField(primary_key=True)
    recipe_instructions = models.TextField()

class Recipe_Ingredients(models.Model):
    recipe_id = models.ForeignKey('Recipe', related_name='recipe_ingredient', on_delete=models.CASCADE)
    ingredient_id = models.ForeignKey('Ingredient', related_name='recipe_ingredient', on_delete=models.CASCADE)
    quantity = models.CharField(max_length=20, null=False)
    
    def __str__(self):
        return f'{self.ingredient_id.ingredient_name} - {self.quantity}'
    
    class Meta:
        unique_together = ['recipe_id', 'ingredient_id'] # Ensures a recipe may only use an ingredient once (not quantity-wise) 
    
class Meal(models.Model):
    meal_id = models.AutoField(primary_key=True)
    meal_name = models.CharField(max_length=256, null=False)   
    recipe_id = models.ForeignKey('Recipe', related_name="meal_recipe", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.meal_name
    
class Meal_Plan(models.Model):
    MEAL_TYPE = (
        ("breakfast", "Breakfast"),
        ("lunch", "Lunch"),
        ("dinner", "Dinner")
    )
    DAY = (
        ("sun", "Sunday"),
        ("mon", "Monday"),
        ("tue", "Tuesday"),
        ("wed", "Wednesday"),
        ("thu", "Thursday"),
        ("fri", "Friday"),
        ("sat", "Saturday"),
    )
    user_id = models.ForeignKey('UserProfile.User', related_name='meal_plan', on_delete=models.CASCADE)
    meal_id = models.ForeignKey('Meal', related_name='meal_plan', on_delete=models.CASCADE)
    meal_type = models.CharField(choices=MEAL_TYPE, max_length=32)
    day = models.CharField(choices=DAY) 
    
    def __str__(self):
        return f'{self.user_id} - {self.meal_id.meal_name} ({self.day} {self.meal_type})'
    
class Meal_Favorites(models.Model):
    user_id = models.ForeignKey('UserProfile.User', related_name='meal_favorite', on_delete=models.CASCADE)
    meal_id = models.ForeignKey('Meal', related_name='meal_favorite', on_delete=models.CASCADE)
    is_ingredients = models.BooleanField(default=False)
    is_calories = models.BooleanField(default=False)
    
    class Meta:
        unique_together = ['user_id', 'meal_id'] # Ensures a user only has 1 entry per meal they've favorited
    
class Hydration_Tracker(models.Model):
    user_id = models.ForeignKey('UserProfile.User', related_name='hydration_tracker', on_delete=models.CASCADE)
    container_size = models.IntegerField()
    water_goal = models.IntegerField()
    active_hours = models.IntegerField()