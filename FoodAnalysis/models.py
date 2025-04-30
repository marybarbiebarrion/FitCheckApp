from django.db import models

class UploadedImage(models.Model):
    image = models.ImageField(upload_to="uploads/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image {self.id} uploaded on {self.uploaded_at}"

class FoodAnalysis(models.Model):
    image = models.ImageField(upload_to='food_images/')
    food_name = models.CharField(max_length=255)
    ingredients = models.TextField()
    allergens = models.TextField()
    alternatives = models.TextField()
    calories = models.IntegerField(null=True, blank=True)
    analyzed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Analysis {self.id} - {self.analyzed_at}"
