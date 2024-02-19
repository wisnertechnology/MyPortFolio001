import logging

from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import send_mail

logger = logging.getLogger(__name__)


def voye_email_avek_ko_html(subjet:str, receivers: list, template:str, context:dict):
    """fonksyon saaa ede nou voye yon email pesonalise avek yon itilizate spesifye"""
    try:
        message = render_to_string(template, context)

        send_mail(
            subjet,
            message,
            settings.EMAIL_HOST_USER,
            receivers,
            fail_silently=True,
            html_message=message
        )
        return True
    except Exception as e:
        logger.error(e)

    return False


