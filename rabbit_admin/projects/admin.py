from django.contrib import admin
from projects.models import Project
from emails_bz.models import EmailBZ
from telegram_message.models import TelegramMessage


class EmailBzInline(admin.TabularInline):
    model = EmailBZ
    fields = ['api_key', 'enabled', 'subject', 'email_from', 'email_to']
    extra = 0
    show_change_link = True
# EmailBzInline


class TelegramMessageInline(admin.TabularInline):
    model = TelegramMessage
    fields = ['name', 'enabled', 'bot_token', 'chat_id']
    extra = 0
    show_change_link = True
# TelegramMessageInline


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'enabled', 'created_at', 'updated_at']
    inlines = [EmailBzInline, TelegramMessageInline]

    def get_changeform_initial_data(self, request):
        return {
            'enabled': True
        }
