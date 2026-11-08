from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Lieu

# Create your views here.

def liste_lieux(request):
    lieux = Lieu.objects.all()
    categorie = request.GET.get("categorie", "")
    recherche = request.GET.get("q", "").strip()

    if categorie:
        lieux = lieux.filter(categorie=categorie)
    if recherche:
        lieux = lieux.filter(
            Q(nom__icontains=recherche) | Q(description__icontains=recherche)
        )

    return render(request, "lieux/liste.html", {
        "lieux": lieux,
        "categories": Lieu.CATEGORIES,
        "categorie_active": categorie,
        "recherche": recherche,
    })


def detail_lieu(request, pk):
    lieu = get_object_or_404(Lieu, pk=pk)
    autres = Lieu.objects.exclude(pk=pk).filter(categorie=lieu.categorie)[:3]
    return render(request, "lieux/detail.html", {
        "lieu": lieu,
        "photos": lieu.photos.all(),
        "autres": autres,
    })
