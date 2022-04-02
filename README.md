# Basic Hello World app with Flask

This repo houses my flask app for the Security Analysis Class[MSBX 5500] of 2022. It is a simple web-application framework, performing a few basic string manipulation.

We have included 3 main app routes, namely:
        <details>
           <summary>"ping" route</summary>
           <p>This route returns "pong!" as the response in a JSON</p>
         </details>
         <details>
          <summary>"word" route</summary>
          <p>This route uses the python <i>requests</i> package to fetch a random word from https://random-word-api.herokuapp.com/word?number=1, which it then changes to upper case and then reverses the characters. The new word and the original word are combined into a JSON file and returned. </p>
        </details>
        <details>
         <summary>"string-count" route</summary>
         <p>The route returns the length of any given string. I used https://reqbin.com/ to enter a string.</p>
        </details>




## Using this repo
### `Docker-Compose command to run the Flask container`
Build and run:

```bash
docker-compose up
# This command publishes through port 5555
# Run this command from the repository terminal/command prompt to build your own container
```

### `Docker-Compose command to execute make-request.py within a running container`
Build and run:

```bash
docker-compose exec web python make-request.py
# This command
# Run this command from the repository terminal/command prompt to build your own container
```
Markup : <details>
           <summary>Title 1</summary>
           <p>Content 1 Content 1 Content 1 Content 1 Content 1</p>
         </details>
