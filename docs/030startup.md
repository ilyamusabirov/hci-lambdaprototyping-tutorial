# Starting Up

0. Get your [AWS](https://aws.amazon.com/console/) security [credentials](https://console.aws.amazon.com/iam/home#/security_credentials),
 put them to the [right place](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html),
 e.g.

 ```bash
 ~/.aws/credentials
 ```

1. Create project folder

2. Create and activate virtual environment in it

```bash
python3 -m venv .venv
. .venv/bin/activate
```

3. Install [chalice](https://aws.github.io/chalice/) into it

```bash
python3 -m pip install chalice
```

4. Create new chalice project

```bash
chalice new-project tg-bot
cd tg-bot
```

4a. Or clone code from tutorial

5. `app.py` contains key code:

```python
from chalice import Chalice
app = Chalice(app_name="tg-notion")
```

Main function if expect POST (e.g. for webhook)

```python
@app.route("/", methods=["POST"])
def main():
    request_body = app.current_request.json_body
    print(request_body)
    return {
        "statusCode": 200
    }
```
 or if expect GET

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

7. Deploy to AWS!

```bash
chalice deploy
```

8. Use returned url to test web API using your favourite cient (if you expect to work with WebAPIs, [Postman](https://www.postman.com/downloads/) is quite cool and intuitive)


* Setting up the environment
    * Linux/Mac/Windows+WSL2 + VSCode
    * colab/deepnote?
* creating the project
* deploying first function
* postman test voila!