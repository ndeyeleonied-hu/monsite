from django.shortcuts import render, get_object_or_404
from .models import Article


def liste_actualites(request):
    articles = Article.objects.filter(publie=True)
    type_actif = request.GET.get("type", "")

    if type_actif in ("actualite", "evenement"):
        articles = articles.filter(type_contenu=type_actif)

    return render(request, "actualites/liste.html", {
        "articles": articles,
        "types": Article.TYPES,
        "type_actif": type_actif,
    })


def detail_actualite(request, pk):
    article = get_object_or_404(Article, pk=pk, publie=True)
    autres = Article.objects.filter(publie=True).exclude(pk=pk)[:3]
    return render(request, "actualites/detail.html", {
        "article": article,
        "autres": autres,
    })