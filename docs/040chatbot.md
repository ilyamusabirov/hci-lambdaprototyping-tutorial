# Chatbot skeleton

## Telegram vs Slack

Currently only Telegram version is covered, but Slack seems to be a solid alternative (no free available API for Whatsapp AFAIK).

In principle, using iPython widgets as interfaces, one can think to create a client in jupyter notebook/collab.

### Telegram bot principles

- [Creating Telegram bots](https://core.telegram.org/bots)

In principle, we can construct and use direct Telegram Web API calls from our Lambda functions, 
but that increases amount of code to develop so using one of Pythons bindings makes sense.

### Webhook mode and python bot packages

Usually bot backends are started as services an use polling to get portions if requests from Telegram.

In FaaS case we need to use webhook mode: set Telegram to transfer each request to the bot to a webhook URL, which AWS API GW will then send to our Lambda function.

Thankfully, Chalice will take care for most of the small details (creatin and setting up API GW, security roles, lambda function, connecting them, returning us URLs).

One important implication of webhook vs polling though that if we use packages to create python bots, we need to ignore the part of the package which starts web service for bot.

Usually good search term for package dosumentation is webhook mode.

* [Python Telegram Bot: Webhook mode](https://github.com/python-telegram-bot/python-telegram-bot/wiki/Webhooks)
* [Python Telegram Bot: General Docs](https://github.com/python-telegram-bot/python-telegram-bot)


## Reacting to first message


## Task ideas

- Render more sofisticated formated prompts, e.g. html+css with `jinja2` in Lambda, png graphs with `matplotlib` or `seaborn`, transform to picture and send via chat bots to preserve formatting/add figures
- Think about voice message and document inputs
- Add intent recognition