from django.contrib import admin

from .models import Allergen, Ingredient, Recipe, Recipe_Ingredients, Meal, Meal_Plan, Hydration_Tracker

class AllergenAdmin(admin.ModelAdmin):
    model = Allergen

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

class HydrationTrackerAdmin(admin.ModelAdmin):
    model = Hydration_Tracker

admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Recipe_Ingredients, RecipeIngredientAdmin)
admin.site.register(Meal, MealAdmin)
admin.site.register(Meal_Plan, MealPlanAdmin)
admin.site.register(Allergen, AllergenAdmin)
admin.site.register(Hydration_Tracker, HydrationTrackerAdmin)