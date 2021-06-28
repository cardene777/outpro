from django.contrib import admin
from .models import Output, Program


class OutputAdmin(admin.ModelAdmin):
    list_display = ("title", "about", "description")


class ProgramAdmin(admin.ModelAdmin):
    list_display = ("output", "name", "description", "code")


admin.site.register(Output, OutputAdmin)
admin.site.register(Program, ProgramAdmin)
