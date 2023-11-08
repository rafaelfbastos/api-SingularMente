from django.contrib import admin
from .models import *


class TelefoneInline(admin.StackedInline):
    model = Phones
    extra = 0


class ContactsAdmin(admin.ModelAdmin):
    inlines = [TelefoneInline]


admin.site.register(Pills)
admin.site.register(Contacts, ContactsAdmin)
admin.site.register(Information)

