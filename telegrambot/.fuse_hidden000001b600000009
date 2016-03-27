import telegram
from telegram.ext import Updater
from parse import parse
from django.conf import settings
# from pyarweb.settings import BOT_TOKEN, PYAR_MODERATION_GROUP
from news.models import NewsArticle

bot = telegram.Bot(token=settings.BOT_TOKEN)

MODERATION_COMMANDS = {"OK": True, "NO": False}


def sendMessage(chat_id, text, parse_mode=None, disable_notification=False):
    """Send new Post to Telegram Group."""
    bot.sendMessage(chat_id=chat_id,
                    **{"text": text,
                       "reply_markup": None,
                       "parse_mode": parse_mode,
                       "disable_web_page_preview": False,
                       "reply_to_message_id": False,
                       "disable_notification": disable_notification})


def moderate(request):
    """Apply moderation and send result to Telegram Group."""
    update = telegram.Update.de_json(request.get_json(force=True))
    if(validateUpdateData(update)):
        id, username, object_type, text = parseText(update.message.reply_to_message.text)
        if object_type == "News":
            NewsArticle.objects.get(pk=id).moderate(MODERATION_COMMANDS[text],
                                                    username)
        # TODO Difundir noticia a traves del bot con sendMessage
        # con chat_id = canal correspondiente
    else:
        bot.sendMessage(chat_id=update.message.chat.id,
                        text="Generic error for now")


def validateUpdateData(update):
    """Validate the message is a reply,
    from the group and with a valid command."""

    if update.message.chat.type != 'group':
        return False
    if update.message.chat.id != settings.PYAR_MODERATION_GROUP:
        return False
    if update.message.reply_to_message is not None:
        return False
    if update.message.text.strip.upper() not in MODERATION_COMMANDS:
        return False

    return True


def parseToText(id_post, username, object_type, post_link):
    """Create a text for Telegram message."""

    return """*Moderación en PyAr*
_ID_: *{id_post}*
_USER_: *{username}*
_TYPE_: *{object_type}*
_LINK_: {post_link}
*OK* | *NO*""".format(**{
                                "id_post": id_post,
                                "username": username,
                                "object_type": object_type,
                                "post_link": post_link})


def parseText(text):
    """Get data from the moderator reply"""
    return parse('Moderación en PyAr\n\
ID: {}\n\
USER: {}\n\
TYPE: {}\n\
LINK: {}\n\
OK | NO', text).fixed
