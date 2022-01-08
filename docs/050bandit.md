# Bot goes bandit

As a first step let's randomize what we return to user:

```python
def random_choice1(update: Update, context:CallbackContext) -> None:
    import random
    options = ['arm1', 'arm2']
    prompts = {
      'arm1': 'This is arm *1*',
      'arm2': 'This _is_ arm _2_'
    }
    arm = random.choice(options)
    update.message.reply_text(prompts[arm], parse_mode="Markdown")
```

Don't forget registering handler for command.

This is the first step to bandit, but due to our request-responce architecture, there is no bandit object existing between function calls.

This means that to create a bandit we will need to add persistence and save and restore bandit state to database for each call.

For that we are going to use AWS DynamoDB, serverless key-value db.

## Adding persistence - DynamoDB

See [dynamodb-setup.ipynb](dynamodb-setup.ipynb) for example of creating DynamoDB table and working with storing bandit data in it before running app examples.

## Advanced references

- [Tutorial](https://aws.amazon.com/blogs/machine-learning/dynamic-a-b-testing-for-machine-learning-models-with-amazon-sagemaker-mlops-projects/) and [Repo](https://github.com/aws-samples/amazon-sagemaker-ab-testing-pipeline) on AB testing (and bandit testing) SageMaker ML models using bandits on Lambda. No chatbots :)

## Task ideas

- Implement other MAB algorithms and extentions (TS, UCB)
- Contextual Bandit and context detection via chatbot for different settings
- Functions for offline learning based on history in DynamoDB
- Prototype texting fixtures: 
    - implement some features to quickly change and load bandit state so not to start from scratch
    - e.g. add 'cheater mode' with commands adding sequence of rewards to some arms, or directly setting up interesting priors