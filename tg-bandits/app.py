from chalice import Chalice
from chalicelib.secret import TG_TOKEN
app = Chalice(app_name="tg-notion")

# @app.route("/")
# def index():
#     return {"hello": "world"}

import json
import requests

from telegram import Update, ForceReply, Bot, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters, CallbackContext

# Create bot, update queue and dispatcher instances
bot = Bot(TG_TOKEN)
dispatcher = Dispatcher(bot, None, workers=0)

### define telegram handler functions
def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr"Hi {user.mention_markdown_v2()}",
        reply_markup=ForceReply(selective=True),
    )

### define telegram handler functions
def key(update: Update, context: CallbackContext) -> None:
    keyboard = [[KeyboardButton("a"), KeyboardButton("b"), KeyboardButton("c"), KeyboardButton("d")]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    user = update.effective_user
    reply_text = fr"Hey {user.mention_markdown_v2()},\select the option",
    print(reply_text)
    update.message.reply_markdown_v2(
        reply_text,
        reply_markup=reply_markup,
    )

def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)
    bot.send_message(update.message.chat.id, f"*echo-sm*", parse_mode="Markdown")

def random_choice1(update: Update, context:CallbackContext) -> None:
    import random
    options = ['arm1', 'arm2']
    prompts = {
      'arm1': 'This is arm *1*',
      'arm2': 'This _is_ arm _2_'
    }
    arm = random.choice(options)
    update.message.reply_text(prompts[arm], parse_mode="Markdown")



### add telegram handlers
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("key", key))
dispatcher.add_handler(CommandHandler("random", random_choice1))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))


# Main
@app.route("/", methods=["POST"])
def main():
    request_body = app.current_request.json_body
    update_object = Update.de_json(request_body, bot)
    print(update_object)
    dispatcher.process_update(update_object)
    return {
        "statusCode": 200
    }

'''
{
  "update_id": 813215257,
  "message": {
    "message_id": 2,
    "from": {
      "id": 132357466,
      "is_bot": false,
      "first_name": "Ilya",
      "username": "ilyamusabirov",
      "language_code": "ru"
    },
    "chat": {
      "id": 132357466,
      "first_name": "Ilya",
      "username": "ilyamusabirov",
      "type": "private"
    },
    "date": 1640076351,
    "text": "/start",
    "entities": [
      {
        "offset": 0,
        "length": 4,
        "type": "bot_command"
      }
    ]
  }
}
'''

