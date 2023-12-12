from django.contrib import admin

# Register your models here.

from .models import Question
#admin.site.register(Question)

from .models import Team, Person, Osoba
admin.site.register(Team)
admin.site.register(Person)



class OsobaAdmin(admin.ModelAdmin):
    list_display = ['imie', 'nazwisko', 'plec', 'stanowisko_id', 'data_dodania']
    list_filter = ['stanowisko', 'data_dodania']
    readonly_fields = ["data_dodania"]
    @admin.display(description='Stanowisko (id)')
    def stanowisko_id(self, obj):
        return f"{obj.stanowisko.nazwa} ({obj.stanowisko.id})"

admin.site.register(Osoba, OsobaAdmin)



from .models import Stanowisko
class StanowiskoAdmin(admin.ModelAdmin):
    filter_list=['nazwa']

admin.site.register(Stanowisko,StanowiskoAdmin)