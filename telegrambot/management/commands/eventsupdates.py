import datetime

from django.core.management.base import BaseCommand
from django.conf import settings
# from pyarweb.settings import PYAR_GENERAL_CHANNEL, PYAR_MODERATION_GROUP
from news.models import NewsArticle
from telegrambot.pyarbot import parseToText, sendMessage


class Command(BaseCommand):

    def handle(self, *args, **options):

        news = NewsArticle.objects.filter(approve=False)

        for new in news:
            url = "192.168.1.139:8000/noticias/" + str(new.pk) + "/moderate"
            msg = parseToText(str(new.pk), new.owner.username, "News", url)
            sendMessage(settings.PYAR_MODERATION_GROUP, msg, parse_mode="Markdown")

