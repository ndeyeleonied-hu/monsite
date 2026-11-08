from django.db import models
from django.utils import timezone

# Create your models here.


class Article(models.Model):
    TYPES = [
        ("actualite", "Actualité"),
        ("evenement", "Événement"),
    ]

    titre = models.CharField(max_length=200)
    type_contenu = models.CharField(max_length=20, choices=TYPES, default="actualite", verbose_name="Type")
    resume = models.CharField(max_length=300, verbose_name="Résumé (pour les cartes)")
    contenu = models.TextField()
    image = models.ImageField(upload_to="actualites/", blank=True)
    date_publication = models.DateTimeField(default=timezone.now, verbose_name="Date de publication")
    date_evenement = models.DateField(null=True, blank=True, verbose_name="Date de l'événement")
    lieu_evenement = models.CharField(max_length=200, blank=True, verbose_name="Lieu de l'événement")
    publie = models.BooleanField(default=True, verbose_name="Publié")

    class Meta:
        ordering = ["-date_publication"]
        verbose_name = "article"
        verbose_name_plural = "actualités et événements"

    def __str__(self):
        return self.titre