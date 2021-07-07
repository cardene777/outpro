from django.contrib import admin
from .models import Output, Program, Good, ReviewCode, Message, Comment


class OutputAdmin(admin.ModelAdmin):
    list_display = ("username", "title", "about", "description", "language", "created_at")


class ProgramAdmin(admin.ModelAdmin):
    list_display = ("username", "output", "name", "description", "code", "good_count", "created_at", "review")


class GoodAdmin(admin.ModelAdmin):
    list_display = ("program", "username")


class ReviewCodeAdmin(admin.ModelAdmin):
    list_display = ("program_id", "username", "review_code", "check")


class MessageAdmin(admin.ModelAdmin):
    list_display = ("review", "username", "message", "check")


class CommentAdmin(admin.ModelAdmin):
    list_display = ("output_id", "program_id", "username", "comment", "created_at")


admin.site.register(Output, OutputAdmin)
admin.site.register(Program, ProgramAdmin)
admin.site.register(Good, GoodAdmin)
admin.site.register(ReviewCode, ReviewCodeAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Comment, CommentAdmin)
