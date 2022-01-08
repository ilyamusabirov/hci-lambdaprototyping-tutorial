# Bot goes bandit

* Exploration vs exploitation
* Sending debug

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