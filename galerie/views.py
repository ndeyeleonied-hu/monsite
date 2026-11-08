from django.shortcuts import render
from .models import Photo

# Create your views here.



def galerie(request):
    photos = Photo.objects.all()
    categorie = request.GET.get("categorie", "")

    if categorie in dict(Photo.CATEGORIES):
        photos = photos.filter(categorie=categorie)

    return render(request, "galerie/liste.html", {
        "photos": photos,
        "categories": Photo.CATEGORIES,
        "categorie_active": categorie,
    })