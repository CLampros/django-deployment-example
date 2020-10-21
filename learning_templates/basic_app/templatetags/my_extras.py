from django import template

register = template.Library()

@register.filter(name="cut")
def cut(value, arg):
    '''
    This cuts all values of "args" from string!
    '''
    return value.replace(arg, '')

#register.filter('cutme', cut)