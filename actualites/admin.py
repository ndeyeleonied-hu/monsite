from django.contrib import admin
from .models import Article
# Register your models here.



@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("titre", "type_contenu", "date_publication", "publie")
    list_filter = ("type_contenu", "publie")
    search_fields = ("titre", "resume")
