
from django.core.management.base import BaseCommand
from django.conf import settings
from news.models import NewsArticle
from jobs.models import Job
from telegrambot.pyarbot import parseToText, sendMessage
from django.utils import timezone
from datetime import timedelta



class Command(BaseCommand):

    def generateurl(self, pk, type_model):
        return "192.168.1.139:8000/" + type_model + "/" + str(pk) + "/moderate"

    def sendmoderate(self, Model, type_model):
        models = Model.objects.filter(approved=False)

        for model in models:
            if (timezone.now() - model.created) > timedelta(days=1):
                url = self.generateurl(model.pk, type_model)
                msg = parseToText(str(model.pk),
                                  model.owner.username,
                                  type_model, url)
                sendMessage(settings.PYAR_MODERATION_GROUP,
                            msg,
                            parse_mode="Markdown")

    def handle(self, *args, **options):

        self.sendmoderate(NewsArticle, "noticias")

        self.sendmoderate(Job, "trabajo")


