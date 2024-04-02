# DevOps Apprenticeship: Project Exercise

> If you are using GitPod for the project exercise (i.e. you cannot use your local machine) then you'll want to launch a VM using the [following link](https://gitpod.io/#https://github.com/CorndelWithSoftwire/DevOps-Course-Starter). Note this VM comes pre-setup with Python & Poetry pre-installed.

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.8+ and install Poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.

## Setting Up Trello Integration

This app uses the Trello API for storing the todo items. 

Set up: 

* A Trello account with Todo board. 
* Generate an API key and Token.

Once you have done this, you will need to update the `.env` file to include your details.


## Running the App

Once the all dependencies have been installed, start the Flask app in development mode within the Poetry environment by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

## Running the Test Suite
To run the tests for the codebase, run the following command:
```
poetry run pytest
```
(Please make sure you have run `poetry add pytest` in the Terminal beforehand to install `pytest`).


## Deploying the application via Ansible to a VM

To deploy the application via Ansible copy the `Ansible` folder to the Host Node, update the inventory file (to include the control node you would like to deploy to) and run the following command:
````
ansible-playbook plybook.yaml -i inventory.yaml
````

> Please note that you will need to have setup passwordless GGH access from the host to each of the managed nodes.

## Build and Running the App via Docker

To build the container for local development, please run:
```bash
docker run --env-file ./.env --publish 8000:5000 -it --mount "type=bind,source=$(pwd)/todo_app,target=/app/todo_app" todo-app:dev
```

For the production container, the build and run commands are:

```bash
docker build --tag todo-app:prod --target production .
```

```bash
docker run --env-file ./.env --publish 8000:5000 -it --mount "type=bind,source=$(pwd)/todo_app,target=/app/todo_app" todo-app:prod
```

## Architectural Diagrams

Architecture digrams can be found in the `diagrams` subfolder. They were built using [https://app.diagrams.net/] (you can use the `.draw.io` file to edit these diagrams).




