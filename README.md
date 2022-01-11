# hci-lambdaprototyping-tutorial

# Serverless Prototyping for computational HCI

[Ilya Musabirov](http://musabirov.info)

## Summary

This is a tutorial and a software prototype for kickstarting serverless (AWS Lambda + Chalice + Python) prototyping with chatbots (Telegram/Slack).

Started as a Final Project for CSC2558 at UofT, it expands on the principles described in [EduCHi2020 discussion paper](https://educhi2020.hcilivingcurriculum.org/wp-content/uploads/2020/04/educhi2020-final38.pdf).

It is intended mostly for HCI/UX students who work with computational interaction (multiarmed bandits, optimization) or program prototypes and want to decrease time-to-prototype 
or time-to-user. Some more reasoning behind this approach to prototypes in [Motivation](docs/010motivation.md). 

Maybe some users find motivation more valuable and inspiring than a particular implementation idea I came up with.

The tutorial contains:

- [docs](docs), explaining critical parts of the approach, and containing some ideas for technical and design exercises
- Jupyter notebooks for some activities (think about each notebook as a prototype of other parts of the system: creating a database and working with gathered data, analytics)
- [code skeleton](tg-bandits) of a Chalice bot backend with stubs of main functions 

## Table of Contents

1. [Motivation for the approach](docs/010motivation.md)
2. [Short intro to serverless architecture](docs/020architecture.md)
3. [Starting up!](docs/030startup.md)
4. [ChatBot](docs/040chatbot.md)
5. [Bot Goes Bandit](docs/050bandit.md)
6. [Exercises, Ideas, Resources, Next Steps](docs/060nextsteps.md)

## Before we start

For practicing with prototyping, you will need:
- an AWS account (all of the key services are in [AWS FreeTier](https://aws.amazon.com/free/))
- notebook service like Deepnote (has some useful features and integrations, free Edu tier) or Colab to expand stubs for working with data and analytics
- Python environment, VSCode or another editor, git

## Feedback

Please, leave issues and questions [here](https://github.com/ilyamusabirov/hci-lambdaprototyping-tutorial/issues).

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/80x15.png" /></a><br />The documents and figures are licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.

--- 

* [Next](docs/010motivation.md)

---
