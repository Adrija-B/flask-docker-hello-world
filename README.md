# Basic Hello World app with Flask

This repo houses my flask app for the Security Analysis Class[MSBX 5500] of 2022


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
