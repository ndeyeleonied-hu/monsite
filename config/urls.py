from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from pages.views import accueil, decouvrir
from leaders.views import liste_leaders, detail_leader
from lieux.views import liste_lieux, detail_lieu
from actualites.views import liste_actualites, detail_actualite

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", accueil, name="accueil"),
    path("decouvrir/", decouvrir, name="decouvrir"),
    path("leaders/", liste_leaders, name="leaders"),
    path("leaders/<int:pk>/", detail_leader, name="leader_detail"),
    path("lieux/", liste_lieux, name="lieux"),
    path("lieux/<int:pk>/", detail_lieu, name="lieu_detail"),
    path("actualites/", liste_actualites, name="actualites"),
    path("actualites/<int:pk>/", detail_actualite, name="actualite_detail"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)