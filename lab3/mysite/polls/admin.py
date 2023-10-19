from django.contrib import admin

from .models import Person
from .models import Team
from .models import Stanowisko
from .models import Osoba

admin.site.register(Person)
admin.site.register(Team)
admin.site.register(Stanowisko)
admin.site.register(Osoba)