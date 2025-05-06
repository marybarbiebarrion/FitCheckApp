from django import template

register = template.Library()

@register.filter
def fix_food_name(value):
    """Replaces underscores with spaces and capitalizes each word"""
    if isinstance(value, str):
        return value.replace('_', ' ').title()
    return value
