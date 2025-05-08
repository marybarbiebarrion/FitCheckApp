from django.urls import path, include

urlpatterns = [
    # Other URLs...
    path('wellness/', include('wellnesstrack.urls', namespace='wellnesstrack')),  # <-- Include with namespace
]