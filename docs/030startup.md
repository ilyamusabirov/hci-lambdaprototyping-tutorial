# Starting Up

## Quick Start

0. Get your [AWS](https://aws.amazon.com/console/) security [credentials](https://console.aws.amazon.com/iam/home#/security_credentials),
 put them to the [right place](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html),
 e.g.

 ```bash
 ~/.aws/credentials
 ```

1. Create a project folder

2. Create and activate virtual environment in it

```bash
python3 -m venv .venv
. .venv/bin/activate
```

3. Install [chalice](https://aws.github.io/chalice/) into it

```bash
python3 -m pip install chalice
```

4. Create a new chalice project

```bash
chalice new-project tg-bot
cd tg-bot
```

4a. Or clone code from the tutorial

5. `app.py` contains key code:

```python
from chalice import Chalice
app = Chalice(app_name="tg-notion")
```

Primary function if we expect POST queries (e.g. for webhook)

```python
@app.route("/", methods=["POST"])
def main():
    request_body = app.current_request.json_body
    print(request_body)
    return {
        "statusCode": 200
    }
```
 or if we expect GET

```python
@app.route("/")
def index():
    return {
        "statusCode": 200
    }
```

6. Test locally:

```bash
chalice local
```
6.1 Just look if there are no annoying errors

6.2 ...or actually test local web API using your favourite client (if you expect to work with WebAPIs, [Postman](https://www.postman.com/downloads/) is quite cool and intuitive)

7. Deploy to AWS!

```bash
chalice deploy
```

Actually, a lot of stuff happens in the background:

- chalice creates deployment package from your virtual environment packages and app code automatically
- creates and saves data on your lambda function, API GW, IAM locally, connects these services to each other
- API GW public URL is created, and the methods we defined (step 5) are set up to accept calls
- public URL we can use for testing or as a webhook is returned to console

8. Use returned URL to test web API using your favourite client (if you expect to work with WebAPIs, [Postman](https://www.postman.com/downloads/) is quite cool and intuitive)

## Hints

- `chalicelib` dir will be embedded to the deployment package. You can use it to structure your code
    - e.g. `chalicelib/secrets/__init__.py` might be a place to store service tokens and variables for a proto
        - don't forget to add this path to `.gitignore` so it wouldn't end up in the public repo
        - better use [AWS way](http://docs.aws.amazon.com/lambda/latest/dg/env_variables.html#env_encrypt) to do that
    - as of now, you can't create multiple AWS Lambda  functions in one Chalice project but can structure your code
- next call to `chalice deploy` will update the function and save the same public API URL
- `chalice logs` should fetch logs from lambda, mind you that they are formed with some delay
    - thus, always use `chalice local` first to catch annoying typos expect

## Next steps

- Use example [code from the project](../tg-bandits/app.py)
- Look at Chalice [tutorials](https://aws.github.io/chalice/tutorials/index.html) and [example apps](https://aws.github.io/chalice/samples/index.html)

## Tricks

- `chalice local` by default starts on `127.0.0.1:8000`. 
    - If you need to change it (e.g. on Windows where WSL2 localhost is different from the host system), use `chalice local --host 0.0.0.0`
    - To discover local IP for WSL2 on Windows, use `wsl hostname -I` in PowerShell
    - Then, use this address in Postman to connect to your local deployment


## TO DO
* Setting up the environment
    * Linux/Mac/Windows+WSL2 + VSCode
    * colab/deepnote?
* creating the project
* deploying first function
* postman test voila!

--- 

* [Next](040chatbot.md)
* [Up](../README.md)

---