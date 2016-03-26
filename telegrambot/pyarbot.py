from pyarweb.settings import BOT_TOKEN, PYAR_GENERAL_CHANNEL, PYAR_MODERATION_GROUP
import telegram
from telegram.ext import Updater
from parse import parse

bot = telegram.Bot(token=BOT_TOKEN)

MODERATION_COMMANDS = ["ACEPTAR", "RECHAZAR"]


def sendMessage(chat_id, text, parse_mode=None, disable_notification=False):
    """Send new Post to Telegram Group."""
    bot.sendMessage(chat_id=chat_id,
                    **{"text": text,
                       "reply_markup": None,
                       "parse_mode": parse_mode,
                       "disable_web_page_preview": False,
                       "reply_to_message_id": False,
                       "disable_notification": disable_notification})


def moderatePost(request):
    """Apply moderation and send result to Telegram Group."""
    update = telegram.Update.de_json(request.get_json(force=True))
    if(validateUpdateData(update)):
        pass
    else:
        bot.sendMessage(chat_id=update.message.chat.id,
                        text="Generic error for now")


def validateUpdateData(update):
    """Validate the message is a reply,
    from the group and with a valid command."""

    if update.message.chat.type != 'group':
        return False
    if update.message.chat.id != PYAR_MODERATION_GROUP:
        return False
    if update.message.reply_to_message is not None:
        return False
    if update.message.text.strip.upper() not in MODERATION_COMMANDS:
        return False

    return True


def parsePostToText(id_post, username, post_link):
    """Create a text for Telegram message from a Pyar Post."""

    return """*Nuevo Post en PyAr*
_ID_: *{id_post}*
_USER_: *{username}*
_LINK_: {post_link}""".format(**{
                                "id_post": id_post,
                                "username": username,
                                "post_link": post_link})


def parseTextToPost(text):
    """Get a Post from de moderator reply"""
    return parse('Nuevo Post en PyAr\n\
ID: {}\n\
USER: {}\n\
LINK: {}', text)
