from django.contrib import admin
from .models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("nom", "email", "sujet", "date_envoi", "lu")
    list_filter = ("lu",)
    list_editable = ("lu",)
    search_fields = ("nom", "email", "sujet")
    readonly_fields = ("nom", "email", "sujet", "contenu", "date_envoi")

    def has_add_permission(self, request):
        return False