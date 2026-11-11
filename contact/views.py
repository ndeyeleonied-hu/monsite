from django.conf import settings
from django.core.mail import BadHeaderError, send_mail
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import MessageForm


def contact(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            if form.cleaned_data.get("site_web"):
                return redirect(f"{reverse('contact')}?envoye=1")

            message = form.save()
            sujet = message.sujet.replace("\r", " ").replace("\n", " ")
            try:
                send_mail(
                    subject=f"[Site Saint-Louis] {sujet}",
                    message=f"De : {message.nom} <{message.email}>\n\n{message.contenu}",
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.CONTACT_EMAIL],
                )
            except (BadHeaderError, OSError):
                pass

            return redirect(f"{reverse('contact')}?envoye=1")
    else:
        form = MessageForm()

    return render(request, "contact/contact.html", {
        "form": form,
        "envoye": request.GET.get("envoye") == "1",
        "site_contact": settings.SITE_CONTACT,
    })