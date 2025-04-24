from django.contrib import admin

from .models import Ingredient, Recipe, Recipe_Ingredients, Meal, Meal_Plan, Meal_Favorites

class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    
class RecipeIngredientAdmin(admin.ModelAdmin):
    model = Recipe_Ingredients
    
class MealAdmin(admin.ModelAdmin):
    model = Meal
    
class MealPlanAdmin(admin.ModelAdmin):
    model = Meal_Plan

class MealFavoriteAdmin(admin.ModelAdmin):
    model = Meal_Favorites


admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Recipe_Ingredients, RecipeIngredientAdmin)
admin.site.register(Meal, MealAdmin)
admin.site.register(Meal_Plan, MealPlanAdmin)
admin.site.register(Meal_Favorites, MealFavoriteAdmin)