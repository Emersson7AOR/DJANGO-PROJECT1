from django import template

register = template.Library()

# Se registra el filtro con su nombre
@register.filter(name="add_attr")
# Funcion con el mismo nombre, que ejecutara acciones 
def add_attr(field, css):
    attrs = {}
    clase, valor = css.split(':') # Se va a dividir por los dos puntos
    attrs[clase] = valor
    return field.as_widget(attrs=attrs)