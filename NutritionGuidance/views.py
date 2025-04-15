from django.http import HttpResponse

def nutrition_guidance(request):
    return HttpResponse('This is the view for Nutrition Guidance.')
