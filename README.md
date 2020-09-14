# Real-time stock chart image generation service with python and FastAPI

This service is a python api that returns real-time stock market charts as an image. It is built with FastAPI and returns data from IEX Cloud for intraday and historical OCHL datasets. Deployment is done through AWS CDK and ECS using the Fargate service type.

## Getting started

Create a new `.env` file.

```
cp .env.example .env
```

Change the values to match your environment.

## Running

The following pipenv scripts have been defined:

```
start
docker_build
docker_run
docker_compose_up
```
To execute `pipenv run <pipenv script name>`

## Credits
Credit to https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker
and https://github.com/sintaro/CDK_ECSFargate_FastAPI
