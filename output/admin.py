from django.contrib import admin
from .models import Output, Program, Good


class OutputAdmin(admin.ModelAdmin):
    list_display = ("username", "title", "about", "description", "language")


class ProgramAdmin(admin.ModelAdmin):
    list_display = ("output", "name", "description", "code", "good_count")


class GoodAdmin(admin.ModelAdmin):
    list_display = ("program", "username")


admin.site.register(Output, OutputAdmin)
admin.site.register(Program, ProgramAdmin)
admin.site.register(Good, GoodAdmin)
