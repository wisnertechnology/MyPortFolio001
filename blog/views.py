from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect


from datetime import datetime

from .itil import voye_email_avek_ko_html




# portfolio/views.py
from django.core.mail import send_mail



# Create your views here.
def acceuil(request):
    return render(request, 'blog/index.html')


def profil(request):
    return render(request, 'index.html')








# ************************ SA SE VIEW KAP JERE ENVOI KOMANTE ITILIZATEA NAN EMAIL NOU *******************************











#-------------------------------------------------------

def submit_comment(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        full_name = request.POST.get('full-name')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Envoi d'email
        send_mail(
            f'Sujet: {subject}',
            f'Nom & Prénom: {full_name}\nEmail: {email}\n\nMessage:\n{message}',
            email,  # L'expéditeur de l'email
            ['votre@email.com'],  # Votre adresse email où vous souhaitez recevoir les commentaires
            fail_silently=False,
        )

        # Rediriger l'utilisateur après l'envoi du commentaire
        return HttpResponse('Email envoye')

    return render(request, 'index.html')  # Remplacez 'index.html' par le chemin réel de votre template
