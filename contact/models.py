
from django.db import models


class Message(models.Model):
    nom = models.CharField(max_length=120)
    email = models.EmailField()
    sujet = models.CharField(max_length=200)
    contenu = models.TextField(verbose_name="Message")
    date_envoi = models.DateTimeField(auto_now_add=True, verbose_name="Date d'envoi")
    lu = models.BooleanField(default=False, verbose_name="Lu")

    class Meta:
        ordering = ["-date_envoi"]
        verbose_name = "message reçu"
        verbose_name_plural = "messages reçus"

    def __str__(self):
        return f"{self.nom} : {self.sujet}"