# fastapi-async-sagemaker-app

A sample application that calls the sagemaker endpoint asynchronously using [FastAPI](https://fastapi.tiangolo.com/).

## Creating a Samemaker endpoint

- Build the container image with a dockerfile.  

```bash
$ docker build -t sagemaker-endpoint-test -f ./Dockerfile.sagemaker .
```

- Push a Docker image to an Amazon ECR repository.

```bash
$ docker push [aws_account_id].dkr.ecr.[region].amazonaws.com/sagemaker-endpoint-test
```

- Create a samemaker endpoint by referring to [this page.](https://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works-deployment.html#how-it-works-hosting)

## Usage

```bash

## Copy the dotenv file
$ cp ./dotenv.sample ./.env

## configure the aws credentials
$ vi .env

## Start the container.
$ docker-compose up -d

## Launch the application
$ docker-compose exec app python main.py

## Execute the script for the test request
$ docker-compose exec app python request_test.py

```
