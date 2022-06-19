# To Do Tutorial

The basic structure of this tutorial is from FSND Course 2: SQL and Database Modeling For The Web. Initial commits in 'todo_example' branch are taken directly from the tutorial, and customized changes are stored in other repositories. 

Detailed notes from the tutorial are stored here, in `todo_example` branch ` README.md`; additional changes can be found in the `main` branch `README.md` 

## `requirements.txt` and prerequisites
This application requires:
- Flask
- Flask-SQLAlchemy
- python3
- Postgresql

## Development Process
import note on convention: terminal commands are appended with `$ ` to differentiate them from other code in these notes, but it is never neccessary to enter `$ `; start the commands in your terminal after the first two chars of the provided command.

### 2.3.9
A Basic Hello World Application
- import statements:
    - import Flask: `from flask import Flask`
    - import Flask-SQLAlchemy: `from flask_sqlalchemy import SQLAlchemy`
- instantiate flask application: `app = Flask(__name__)`
    - pass `__name__` as parameter
    - sets app if `app.py` is the name of your file (in this example, it is)
- define flask route: `@app.route('/')`
    - `@app` is a python decorator
    - accepts the `index()` function as a callback that is invoked when a request to the route `/` comes in from the client
    - it wraps the `index()` function
    - `@app.route('/')` tells the app the function `index()` is a route
    - `'/'` is a default 'home' route; `@app.route()` takes a path as a parameter
- define `index()` function:
    - listens to connections to the root (`/`) route
    - determines behavior based on function definition

At this point you can run the application:
0. (optional but highly reccomended): create virtual enviornment and enter it
    - create enviornment: `$ pip3 -m venv .env`
        - `.env` is the location of our new enviornment
    - enter/run venv: `$ source .env/bin/activate`
        - if you used a different name/location than `.env` replace it in the path as `$ [location]/bin/activate`
    - when you eventually need to leave the enviornment, use `$ deactivate`
1. set FLASK_APP to name of application: `$ export FLASK_APP=<filename>.py`
2. (optional) create virtual enviornment; set debug and development within enviornment:
    - set debug to true to refresh server on change `$ export FLASK_DEBUG=True`
    - set development env `$ export FLASK_ENVIORNMENT=development`
3. start flask server: `$ flask run`
4. check the server in your browser at the address http://localhost:5000