from django.template import Library

register = Library()


@register.filter()
def get_replace(slug: str):
    return slug.replace(" ", "-")
