from chalice import Chalice
from chalicelib.secret import TG_TOKEN
app = Chalice(app_name="tg-notion")

# @app.route("/")
# def index():
#     return {"hello": "world"}

import json
import requests

from telegram import Update, ForceReply, Bot, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler

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

## This handler requires created DynamoDB table and created bandit record
BANDIT_DATA_TABLE = 'tg-bandits-bandit1'
BANDIT_NAME = 'test_epsilon_greedy_1'
### Move this part to header/separate module. Combined here for handlers versioning in the tutorial 
import boto3
from decimal import Decimal
import json
import random
def reply_bandit_policy(update: Update, context:CallbackContext) -> None:
    ddb = boto3.resource('dynamodb')
    bandit_key = {'bandit_id': BANDIT_NAME,
                                    'creation_date': '2021-01-07 00:00:01'}
    table = ddb.Table(BANDIT_DATA_TABLE)
    r = table.get_item(Key=bandit_key)
    item = r['Item']
    print(item)
    update.message.reply_text(str(item))

def random_choice_bandit1(update: Update, context:CallbackContext) -> None:
    """Src: https://github.com/python-telegram-bot/python-telegram-bot/blob/master/examples/inlinekeyboard.py
      Presenting options from epsilon-greedy bandit persisted in DynamoDB, showing inline keyboard for reward
    """
    ddb = boto3.resource('dynamodb')
    bandit_key = {'bandit_id': BANDIT_NAME,
                                    'creation_date': '2021-01-07 00:00:01'}
    table = ddb.Table(BANDIT_DATA_TABLE)
    r = table.get_item(Key=bandit_key)
    item = r['Item']
    print(item)
    # update.message.reply_text(str(item))
    eps = item['epsilon']
    p = random.random()
    print(p, eps)
    arms = item['state']['arms']
    arm_ids = list(arms.keys())
    arm_rewards = {arm:state['reward']/(state['n']+1) for (arm, state) in arms.items()}
    if p < eps:
      choice = random.choice(arm_ids)
    else:
      choice = max(arm_rewards, key = arm_rewards.get)

    prompt = arms[choice]['text']

    keyboard = [
      [
        InlineKeyboardButton("Yes", callback_data=f'{choice}-1'), 
        InlineKeyboardButton("No", callback_data=f'{choice}-0')]
      ]
    reply_markup = InlineKeyboardMarkup(keyboard, resize_keyboard=True)
    user = update.effective_user
    # print(reply_markup)
    # print('---\n')
    # print(prompt)
    update.message.reply_markdown_v2(
        f"{prompt}\n Do you like it?",
        reply_markup=reply_markup,
    )
def button(update: Update, context: CallbackContext) -> None:
    """Src: https://github.com/python-telegram-bot/python-telegram-bot/blob/master/examples/inlinekeyboard.py
       Working with response to bandit prompt. Now passing data is really ugly (string callback + split)
    """
    query = update.callback_query
    
    data = query.data.split('-')
    choice = data[0]
    reward = data[1]

    ddb = boto3.resource('dynamodb')
    bandit_key = {'bandit_id': BANDIT_NAME,
                                    'creation_date': '2021-01-07 00:00:01'}
    table = ddb.Table(BANDIT_DATA_TABLE)
    r = table.get_item(Key=bandit_key)
    item = r['Item']

    item['state']['arms'][choice]['reward'] += Decimal(reward)
    item['state']['arms'][choice]['n'] += Decimal(1)
    response = table.put_item(
      Item = item
    )
    #query.answer(text=f"Selected option: {str(query.data)}, {response}")
    query.edit_message_text(text=f"Selected option: {str(query.data)},\n{response}")
    # update.message.reply_text(f"Selected option: {str(query.data)}, {response}")


### add telegram handlers
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("key", key))
dispatcher.add_handler(CommandHandler("report", reply_bandit_policy))
dispatcher.add_handler(CommandHandler("random", random_choice_bandit1))
dispatcher.add_handler(CallbackQueryHandler(button))
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

