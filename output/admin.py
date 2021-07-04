from django.contrib import admin
from .models import Output, Program, Good, Message, Comment


class OutputAdmin(admin.ModelAdmin):
    list_display = ("username", "title", "about", "description", "language")


class ProgramAdmin(admin.ModelAdmin):
    list_display = ("output", "name", "description", "code", "good_count")


class GoodAdmin(admin.ModelAdmin):
    list_display = ("program", "username")


class MessageAdmin(admin.ModelAdmin):
    list_display = ("review", "username", "message", "check")


class CommentAdmin(admin.ModelAdmin):
    list_display = ("output_id", "program_id", "username", "comment")


admin.site.register(Output, OutputAdmin)
admin.site.register(Program, ProgramAdmin)
admin.site.register(Good, GoodAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Comment, CommentAdmin)
