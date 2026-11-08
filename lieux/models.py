from django.db import models


class Lieu(models.Model):
    CATEGORIES = [
        ("patrimoine", "Patrimoine"),
        ("nature", "Nature"),
        ("culture", "Culture"),
        ("gastronomie", "Gastronomie"),
    ]

    nom = models.CharField(max_length=200)
    categorie = models.CharField(max_length=20, choices=CATEGORIES)
    description = models.TextField(verbose_name="Description courte (pour les cartes)")
    photo = models.ImageField(upload_to="lieux/", verbose_name="Photo principale")
    adresse = models.CharField(max_length=255, blank=True)
    a_la_une = models.BooleanField(default=False, verbose_name="Afficher à la une")
    date_ajout = models.DateTimeField(auto_now_add=True)
    adresse = models.CharField(max_length=255, blank=True)
    latitude = models.FloatField(null=True, blank=True, help_text="Exemple : 16.0258")
    longitude = models.FloatField(null=True, blank=True, help_text="Exemple : -16.5011")

    # Informations de la fiche détaillée
    presentation = models.TextField(blank=True, verbose_name="Présentation détaillée")
    comment_y_aller = models.TextField(blank=True, verbose_name="Comment s'y rendre")
    meilleure_periode = models.CharField(max_length=200, blank=True, verbose_name="Meilleure période")
    duree_visite = models.CharField(max_length=100, blank=True, verbose_name="Durée conseillée")
    conseils = models.TextField(blank=True, verbose_name="Conseils pratiques")

    class Meta:
        verbose_name_plural = "lieux"
        ordering = ["nom"]

    def __str__(self):
        return self.nom


class PhotoLieu(models.Model):
    lieu = models.ForeignKey(Lieu, on_delete=models.CASCADE, related_name="photos")
    image = models.ImageField(upload_to="lieux/galerie/")
    legende = models.CharField(max_length=200, blank=True)
    ordre = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["ordre"]
        verbose_name = "photo supplémentaire"
        verbose_name_plural = "photos supplémentaires"

    def __str__(self):
        return f"{self.lieu.nom} - photo {self.ordre}"