# python-api-tests
A pet project for creating the infrastructure for the testing of API using Python + Requests stack.

## Before the start

- Clone the test app [Sock Shop: A Microservice Demo Application](https://github.com/microservices-demo/microservices-demo) 
- Deploy the app

For instance, I used docker-compose and ran it locally
```sh
cd microservices-demo/deploy/docker-compose/
docker-compose up -d
```
Verify the deployment by navigating to your server address in
your preferred browser.

```sh
http://localhost/
```

**More info about the [Sock Shop: A Microservice Demo Application](https://microservices-demo.github.io)**


## Setup

Install the env
```sh
pipenv install
```
if the virtualenv is already activated, you can also use:
```sh
pipenv sync
```

It should install all required packages.
`PAY ATETNION` sometimes you should install the **pydantic-factories** package separate and manually
```sh
pip install pydantic-factories
```

## Run tests

From the root of the project run 
```sh
pytest tests -sv --alluredir=allure_results
```
The running with **-sv --alluredir=allure_results** keys needed for test reporting.

(After this running of the command, tests should be run and the **allure_results** folder should appear in the framework)

## Generate Results

From the root of the project run 
```sh
allure serve /Users/valeriisynenko/PycharmProjects/apiTestsPython/allure_results
```
After this tests should open your browser with an allure report of the previous test run.
More info about [Allure Report](https://qameta.io/allure-report/)
