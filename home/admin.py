from django.contrib import admin
from .models import Gender,Passport, Nationality, Languages, Person
# Register your models here.

admin.site.register(Gender)
admin.site.register(Passport)
admin.site.register(Nationality)
admin.site.register(Languages)
admin.site.register(Person)

