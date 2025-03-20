from django.db import models

class FoodAnalysis(models.Model):
    image = models.ImageField(upload_to='uploads/')
    analyzed_at = models.DateTimeField(auto_now_add=True)
    ingredients = models.TextField()
    allergens = models.TextField()
    alternatives = models.TextField()

    def __str__(self):
        return f"Analysis {self.id} - {self.analyzed_at}"