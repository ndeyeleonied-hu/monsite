from django.shortcuts import render
from django.urls import reverse
from django.utils.text import Truncator
from lieux.models import Lieu
from actualites.models import Article


def accueil(request):
    lieux = Lieu.objects.filter(a_la_une=True)[:3]
    actualites = Article.objects.filter(publie=True)[:3]
    return render(request, "pages/accueil.html", {
        "lieux": lieux,
        "actualites": actualites,
    })


def decouvrir(request):
    return render(request, "pages/decouvrir.html")


def carte(request):
    avec_position = Lieu.objects.filter(latitude__isnull=False, longitude__isnull=False)

    donnees = [
        {
            "nom": lieu.nom,
            "categorie": lieu.categorie,
            "categorie_nom": lieu.get_categorie_display(),
            "lat": lieu.latitude,
            "lng": lieu.longitude,
            "url": reverse("lieu_detail", args=[lieu.pk]),
            "photo": lieu.photo.url,
            "description": Truncator(lieu.description).words(20),
        }
        for lieu in avec_position
    ]

    return render(request, "pages/carte.html", {
        "donnees": donnees,
        "categories": Lieu.CATEGORIES,
        "total": avec_position.count(),
        "sans_position": Lieu.objects.count() - avec_position.count(),
    })