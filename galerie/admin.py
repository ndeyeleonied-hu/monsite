from django.contrib import admin
from .models import Photo
# Register your models here.



@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ("titre", "categorie", "ordre")
    list_editable = ("ordre",)
    list_filter = ("categorie",)
    search_fields = ("titre", "legende")