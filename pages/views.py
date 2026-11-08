from django.shortcuts import render
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