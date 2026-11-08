from django.shortcuts import render

# Create your views here.
def accueil(request):
    return render(request, "pages/accueil.html")

def decouvrir(request):
    return render(request, "pages/decouvrir.html")
