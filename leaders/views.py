from django.shortcuts import render, get_object_or_404
from .models import Leader


def liste_leaders(request):
    principaux = Leader.objects.filter(principal=True)
    autres = Leader.objects.filter(principal=False)

    groupes = []
    for code, nom in Leader.GROUPES:
        membres = autres.filter(groupe=code)
        if membres.exists():
            groupes.append({"nom": nom, "membres": membres})

    return render(request, "leaders/liste.html", {
        "principaux": principaux,
        "groupes": groupes,
    })


def detail_leader(request, pk):
    leader = get_object_or_404(Leader, pk=pk)
    return render(request, "leaders/detail.html", {"leader": leader})