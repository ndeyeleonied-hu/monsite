from django.contrib import admin
from .models import Lieu, PhotoLieu


class PhotoLieuInline(admin.TabularInline):
    model = PhotoLieu
    extra = 3
@admin.register(Lieu)
class LieuAdmin(admin.ModelAdmin):
    list_display = ("nom", "categorie", "a_la_une")
    list_filter = ("categorie", "a_la_une")
    search_fields = ("nom",)
    inlines = [PhotoLieuInline]