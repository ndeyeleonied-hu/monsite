from django.db import models


# Create your models here.
class Leader(models.Model):
    GROUPES = [
        ("direction", "Direction"),
        ("conseillers", "Conseillers"),
        ("partenaires", "Partenaires"),
    ]

    nom = models.CharField(max_length=150)
    fonction = models.CharField(max_length=150)
    groupe = models.CharField(max_length=20, choices=GROUPES, default="direction")
    photo = models.ImageField(upload_to="leaders/")
    biographie = models.TextField()
    citation = models.CharField(max_length=300, blank=True)
    email = models.EmailField(blank=True)
    facebook = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    principal = models.BooleanField(default=False, verbose_name="Mettre en avant en haut de page")
    ordre = models.PositiveIntegerField(default=0, help_text="Plus le nombre est petit, plus il apparaît en premier")

    class Meta:
        ordering = ["ordre", "nom"]
        verbose_name_plural = "leaders"

    def __str__(self):
        return self.nom