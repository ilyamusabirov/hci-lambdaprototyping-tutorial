# hci-lambdaprototyping-tutorial

# Serverless Prototyping for computational HCI

[Ilya Musabirov](http://musabirov.info)

This is a tutorial/JOLT for kickstarting serverless (AWS Lambda + Chalice + Python) prototyping with chatbots (Telegram/Slack).

It is intended mostly for HCI/UX students, who work with computational interaction (multiarmed bandits, optimization) or program prototypes and want to decrease time-to-prototype 
or time-to-user. Some more reasoning behind this approach to prototypes in [Motivation](docs/010motivation.md). 

Maybe some of the users find motivation more useful and ispiring than a particular implementation ideas I came up with.

The tutorial contains:

- [docs](docs), explaining key parts of the approach, and containing some ideas for technical and design exercises
- Jupyter notebooks for some activities (think about each notebook as a ptototype of other parts of the system: creating database and working with gathered data, analytics)
- [skeleton](tg-bandits) of a Chalice bot backend with stubs of key functions 

## Table of Contents

1. [Motivation for the approach](docs/010motivation.md)
2. [Short intro to serverless architecture](docs/020architecture.md)
3. [Starting up!](docs/030startup.md)
4. [ChatBot](docs/040chatbot.md)
5. [Bot Goes Bandit](docs/050bandit.md)
6. [Exercises, Ideas, Resources, Next Steps](docs/060nextsteps.md)

For practicing with prototyping you will need:
- an AWS account (all of the key services are in [AWS FreeTier](https://aws.amazon.com/free/))
- notebook service like Deepnote (has some useful features and integrations, free edu tier) or Colab to expand stubs for working with data and analytics
- Python environment, VSCode or other editor, git


* Why chatbots
