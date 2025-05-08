from django.urls import path, include

urlpatterns = [
    # Other URLs...
    path('wellness/', include('wellnesstracker.urls', namespace='wellnesstracker')),  
]