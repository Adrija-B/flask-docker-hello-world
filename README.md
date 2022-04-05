# Basic Hello World app with Flask

This repo houses my flask app for the Security Analysis Class[MSBX 5500] of 2022. It is a simple web-application framework, currently performing a few basic string manipulation.

We have included 3 main app routes, namely:
        <details>
           <summary>`ping` route</summary>
           <p>This route returns "pong!" as the response in a JSON</p>
         </details>
         <details>
          <summary>`word` route</summary>
          <p>This route uses the python *requests* package to fetch a random word from [Random Word API](https://random-word-api.herokuapp.com/word?number=1 "Link Title"), which it then changes to upper case and then reverses the characters. The new word and the original word are combined into a JSON file and returned. </p>
        </details>
        <details>
         <summary>`string-count` route</summary>
         <p>The route returns the length of any given string, again in JSON format. I used https://reqbin.com/ to enter a string and check.</p>
        </details>

- - - -
## REPO CONTENTS

FILENAME  | CONTENT
------------- | -------------
.GITIGNORE  | Helps exclude stuff that needs to be excluded.
Dockerfile  | Runs ``` FROM``` python:3.9-slim-bullseye and ```COPY``` the local requirements.txt and pip install it. We have added ```CMD``` ["flask", "run"], that runs the flask app and it binds to all interfaces (i.e., ```host=0.0.0.0```)
Requirements.txt  | Includes all necessary packages, version-pinned.
docker-compose.yml  | build the local (.) Dockerfile publish container port 5000 to host port 5555 mount the current directory into whatever your Dockerfile WORKDIR is.
app.py  | The Flask APP.
make-request.py  | Use the *requests* library to hit each of the flask app routes.
templates  | Stores the templates for the app routes

- - - -

## Using this REPO
### `Docker-Compose command to run the Flask container`
Build and run:

```bash
docker-compose up
# This command publishes through local port 5555
# Run this command from the repository terminal/command prompt to run the flask container
```

### `Docker-Compose command to execute make-request.py within a running container`
Build and run:

```bash
docker-compose exec web python make-request.py
# This command
# Run this command from the repository terminal/command prompt
```
