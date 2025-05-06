from django.db import models

class UploadedImage(models.Model):
    image = models.ImageField(upload_to="uploads/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image {self.id} uploaded on {self.uploaded_at}"

class FoodAnalysis(models.Model):
    image = models.ImageField(upload_to='food_images/')
    food_name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    ingredients = models.TextField()
    allergens = models.TextField()
    alternatives = models.TextField()
    calories = models.IntegerField(null=True, blank=True)
    protein = models.FloatField(null=True, blank=True)  # Protein in grams
    carbohydrates = models.FloatField(null=True, blank=True)  # Carbs in grams
    fats = models.FloatField(null=True, blank=True)  # Fats in grams
    fiber = models.FloatField(null=True, blank=True)  # Fiber in grams
    sugars = models.FloatField(null=True, blank=True)  # Sugars in grams
    sodium = models.FloatField(null=True, blank=True)  # Sodium in mg
    analyzed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Analysis {self.id} - {self.analyzed_at}"
