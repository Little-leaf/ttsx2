from django.template import Library

register = Library()


@register.filter
def create_image_name(index):
    return 'images/banner0' + str(index) + '.jpg'


@register.filter
def str_int(my_str):
    return int(my_str)