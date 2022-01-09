# Motivation

## Why (sometimes) software prototyping

Prototyping is an essential part of the design thinking/design research loop, more so is iterative prototyping. Throughout the years, many people in HCI research and practice developed desiderata, among which:

1. They should represent and communicate the essence of the design hypotheses we test to stakeholders and users.
2. The media and prototyping process should ensure that they are quickly produced in multiplicity to represent the range of design alternatives sprung from the hypotheses.
3. They should be easily updated, changed and thrown away when (not if!) necessary.

For quite some time, the consensus is that low technology prototyping, in many cases, better satisfies these requirements, especially in early research stages when the design space is broad, so paper, markers and stickers dominate more hi-fi solutions.

Some reasons behind that are:

1. The ubiquity of low-tech solutions.
2. Easiness to engage users how are not IT professionals.
3. Lower psychological commitment of process participants to something done in low details and without much effort as opposed to _sunk costs_ associated with the ideas and artifacts we spend time and effort to come up with.

On the contrary, software prototypes were considered a high-investment, low-changeability approach, too high UI fidelity approach, not suitable for early design stages. Here it is important to note that a high level of effort is also (mostly) due to all of the layers of the environment and infrastructure needed to run up the only thing we care about: some lines of interaction logic code required to test out hypotheses.

However, as design thinkers, we should always test and re-test solutions to old problems and requirements if they help us better do our job in some contexts.

I argue that three recent trends lay out the case to reconsider software prototyping as _heavy_ technology for late project stages.

1. Cloud computing technologies, like the Serverless/Function-as-a-service approach, allow us to substantially decrease infrastructure starting costs for prototyping and time-to-prototype.
2. Messengers as a pervasive channel to (repeatedly) access users easier and with low starting requirements on interface details.
3. Rise of data-/AI-based designs in UX portfolios, where the user should interact with an algorithm on different stages of product development when many other aspects of the product are not done.

Thus, this tutorial describes using a serverless approach to kickstart creating quick-n-dirty software prototypes and interacting with users via messengers.

## What's and Why Serverless

The main idea of cloud computing is giving up responsibility for some of the infrastructure layers to the provider instead of taking care of it ourselves. And the essence of it is the Function-as-a-Service approach. With FaaS, our responsibility is as close as possible to writing down the code we need to represent our interaction logic as functions in Python (JS, Go, ...). The services (AWS Lambda, Azure Functions, etc.) will allow us to ignore (or low-invest) many of the rest things traditionally associated with software development.

Suppose our communication channel with the user can also work API style, e.g. in dialogue interaction mode. In that case, life gets even easier, as request-response style is what we can very easily support serverless way. Note that even if our final product is supposed to work not via messenger, dialogue interaction gives us many affordances to test crucial logic even with low effort.

## Why Lambda + Chalice

This tutorial will use AWS serverless service Lambda and Lambda-centred Python framework Chalice, which decreases the entry barrier starting to code with Lambda substantially. Those more inclined to Azure or other infrastructures can look into Azure Functions or other analogs and find relevant frameworks.

A good bonus is that Lambda, DynamoDB and some other components can be (with some limits, usually enough for prototyping) used as a part of AWS FreeTier.

## Why chatbots

- No ideal interaction-only prototype but (simple request-response) chatbots are pretty close
    - you can outline dialogue-based interaction strict from a conceptual model (more likely verb/task than noun/entity-based) and scenario outlines
    - you can mix low-def and hi-def parts (e.g. rendering real output forms and sending via messenger)
- If integrated into the right channel with chances of being a part of user flow (Telegram, Slack), it might more likely to sustain longitudinal interaction than a web app
- Can initiate interactions (prompts, notifications)
