# Chatbot skeleton

## Telegram vs Slack

Currently, only the Telegram version is covered, but Slack seems to be a solid alternative (no free available API for Whatsapp, AFAIK).

In principle, using iPython widgets as interfaces, one can think to create a client in a Jupyter notebook/Collab.

### Telegram bot principles

- [Creating Telegram bots](https://core.telegram.org/bots)

In principle, we can construct and use direct Telegram Web API calls from our Lambda functions, 
but that increases the amount of code to develop, so using one of Pythons bindings makes sense.

You will need a secret bot token as a result of creating a bot with [BotFather](https://telegram.me/botfather).

You can put it to

```bash
chalicelib/secret/__init__.py
```

to use in your code as

```python
from chalicelib.secret import TG_TOKEN
```

### Webhook mode and python bot packages

Usually, bot backends are started as services and use polling to get portions of requests from Telegram (see [ch 2](020architecture.md) for the overview).

In the FaaS case, we need to use webhook mode: set Telegram to transfer each request to the bot to a webhook URL, which AWS API GW will then send to our Lambda function.

Thankfully, Chalice will take care of most small details (creating and setting up API GW, security roles, lambda function, connecting them, returning us URLs).

One crucial implication of webhook vs polling is that if we use packages to create python bots, we need to ignore the part of the package that starts web service for a bot.

Usually, a good search term for package documentation is the "webhook mode".

* [Python Telegram Bot: Webhook mode](https://github.com/python-telegram-bot/python-telegram-bot/wiki/Webhooks)
* [Python Telegram Bot: General Docs](https://github.com/python-telegram-bot/python-telegram-bot)

After setting up your back end in Chalice and creating the bot, you want to [set up web hook](docs/webhook-setup.ipynb) to point to your Lambda function (assuming its URL is in `LAMBDA_URL`)

Starting from that point, your Telegram bot should work with your backend.

## Code structure for bot

With `python-telegram-bot`, our code contains multiple parts:

### Main Lambda request handler

This is where requests are sent from Telegram via webhook.

```python
@app.route("/", methods=["POST"])
def main():
    request_body = app.current_request.json_body
    update_object = Update.de_json(request_body, bot)
    print(update_object)
    dispatcher.process_update(update_object)
    return {
        "statusCode": 200
    }
```

After getting `request_body`, we manually call bot `dispatcher` to process updates we got.

This process looks for handlers for different types of updates.

### Telegram bot dispatcher handlers registration

```python
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("key", key))
dispatcher.add_handler(CommandHandler("random", random_choice1))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
```
After matching with the correct handler, the update looks for a particular function.

### Telegram bot handler functions

```python
### define telegram handler functions
def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr"Hi {user.mention_markdown_v2()}",
        reply_markup=ForceReply(selective=True),
    )
```

Note that to reply to the user, we use bot methods to send messages, not return values from functions.

## Task ideas

- Render more sophisticated formated prompts, e.g. html+css with `jinja2` in Lambda, png graphs with `matplotlib` or `seaborn`, transform to picture and send via chatbots to preserve formatting/add figures
- Think about voice message and document inputs
- Add intent recognition

--- 

* [Next](050bandit.md)
* [Up](../README.md)

---
