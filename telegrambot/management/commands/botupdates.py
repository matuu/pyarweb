import datetime

from django.core.management.base import BaseCommand
from django.conf import settings
# from pyarweb.settings import BOT_TOKEN
from news.models import NewsArticle
import telegram
from telegrambot.pyarbot import moderate


class Command(BaseCommand):

    def handle(self, *args, **options):
        bot = telegram.Bot(token=settings.BOT_TOKEN)
        updates = bot.getUpdates()
        for update in updates:
            moderate(None, update=update)
        # news = NewsArticle.objects.filter(approve=False)

        # for new in news:
        #     url = "192.168.1.139:8000/noticias/" + str(new.pk) + "/moderate"
        #     msg = parseToText(str(new.pk), new.owner.username, "News", url)
        #     sendMessage(PYAR_MODERATION_GROUP, msg, parse_mode="Markdown")

