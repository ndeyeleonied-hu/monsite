from django.contrib import admin
from .models import Leader
# Register your models here.
@admin.register(Leader)
class LeaderAdmin(admin.ModelAdmin):
    list_display = ("nom", "fonction", "groupe", "principal", "ordre")
    list_editable = ("ordre",)
    list_filter = ("groupe", "principal")
    search_fields = ("nom", "fonction")