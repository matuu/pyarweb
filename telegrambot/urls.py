from django.conf.urls import patterns, url
from .views import (
    BotMessage
)


urlpatterns = patterns('',
                       url(r'^$', BotMessage.as_view(),
                           name='bot_message')
                       )
