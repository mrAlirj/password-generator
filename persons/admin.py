from django.contrib.admin import ModelAdmin, register


from persons.models import Person

@register(Person)
class PersonAdmin(ModelAdmin):
    list_display = ('name', 'birthdaye')
    icon_name = 'face'
