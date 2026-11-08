from django.db import models

# Create your models here.


class Photo(models.Model):
    CATEGORIES = [
        ("patrimoine", "Patrimoine"),
        ("nature", "Nature"),
        ("culture", "Culture"),
        ("vie", "Vie quotidienne"),
        ("evenements", "Événements"),
    ]

    titre = models.CharField(max_length=200)
    categorie = models.CharField(max_length=20, choices=CATEGORIES)
    image = models.ImageField(upload_to="galerie/")
    legende = models.CharField(max_length=300, blank=True, verbose_name="Légende")
    credit = models.CharField(max_length=200, blank=True, verbose_name="Crédit photo (auteur ou source)")
    ordre = models.PositiveIntegerField(default=0)
    date_ajout = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["ordre", "-date_ajout"]
        verbose_name = "photo"
        verbose_name_plural = "photos"

    def __str__(self):
        return self.titre