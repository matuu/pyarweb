import datetime

from django.core.management.base import BaseCommand

from pyarweb.settings import PYAR_GENERAL_CHANNEL, PYAR_MODERATION_GROUP
from news.models import NewsArticle
from telegrambot.pyarbot import parseToText, sendMessage


class Command(BaseCommand):

    def handle(self, *args, **options):

        news = NewsArticle.objects.filter(approve=False)

        for new in news:
            url = "127.0.0.1:8000/noticias/" + str(new.pk) + "/moderate"
            msg = parseToText(str(new.pk), new.owner.username, "News", url)
            sendMessage(PYAR_MODERATION_GROUP, msg, parse_mode="Markdown")

