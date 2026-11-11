from django import forms
from .models import Message


class MessageForm(forms.ModelForm):
    site_web = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"tabindex": "-1", "autocomplete": "off"}),
    )

    class Meta:
        model = Message
        fields = ["nom", "email", "sujet", "contenu"]
        labels = {
            "nom": "Votre nom",
            "email": "Votre adresse email",
            "sujet": "Sujet",
            "contenu": "Votre message",
        }
        widgets = {
            "nom": forms.TextInput(attrs={"class": "form-control form-control-lg"}),
            "email": forms.EmailInput(attrs={"class": "form-control form-control-lg"}),
            "sujet": forms.TextInput(attrs={"class": "form-control form-control-lg"}),
            "contenu": forms.Textarea(attrs={"class": "form-control form-control-lg", "rows": 6}),
        }
        