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
- import note on convention: terminal commands are appended with `$ ` to differentiate them from other code in these notes, but it is never neccessary to enter `$ `; start the commands in your terminal after the first two chars of the provided command. 
- similarly, commands intended to be run inside the python interpreter are prepended with `>>> `
- it is assumed that all cli commands and actions are executed from the root folder since this project has an extremely basic structure

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

### 2.3.9b
- add `__main__` block to end of code and specify an alternate port if you want:
        ```
        if __name__=='__main__':
            app.run(port=5001)
        ```
- now, you can also run the app with `python3 app.py`
- check this in your browser at the address http://localhost:5001 (or whatever port you chose)

### 2.3.10
- import flask SQLAlchemy library: `from flask_sqlalchemy import SQLAlchemy`
- link to flash application to begin using SQLAlchemy: `app = Flask(__name__)`
- connect to postgres database from our flask application: `app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://<username>@<host>:<port>/<dbname>`
- configuration variable URI
    - dialect: database dialect
    - username: could be `postgres` or name of the server
    - password: optional
    - host: address, possibly `localhost`
    - port: connection of port used on host
    - database name: name of your database
- ! configure DBAPI specification (optional): add plus sign and name after dialect, ex. `postgres+psycopg2://<username>@<host>:<port>/<dbname>`
- `db = SQLAlchemy(app)`: set db equal to sqlalchemy and pass in flask application; links instance of db we can interact with to our flask application

### 2.3.11
- `class Person(db.Model)`: create model by declaring class which inherits sqlalchemy class `Model` and define columns as variables
    - define primary key attribute for class: `id = db.Column(db.Integer, primary_key=True)`
    - define a string attribute named `name`: `name = db.Column(db.String(), nullable=False)`
- set table name manually: `__tablename__ = '<tablename>'`
    - in this case `Person` SQLAlchemy model will be mapped to `person`
    - default tablename is the name of the table for you and set it equal to the lowercase version of your class

### 2.3.12
- use `db.create_all()` to actually create database model
- add it after your defined models

## 2.3.13
- select first record: `<Model_name>.query.first()`
1. store query response as variable: `person = Person.query.first()`
2. change return statement in `index()` block to `return 'Hello' + person`
(also added `app.config[SQLALCHEMY_TRACK_MODIFICATIONS]=False` because it was v annoying and realized previously mentioned `from flask_sqlalchemy import SQLAlchemy` was ommitted in previously committed code)

## 2.3.14
- add `__repr__(self)` to `Person` model: `f'Person ({self.id}): {self.name}'`

## 2.5.2
1. Create `templates` folder @ .`templates/pages` and store `index.html` there
2. Create `index()` route to return HTML template file
    ```
    from flask import Flask
    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template('index.html')
    ```
3. Create Jinja loop to display variables passed through the template
    ```
    (some msg indicating success)
    ...
    <ul>
        <br>{% for d in data %}
        <br><li>{{d.description}}</li>
        <br>{% endfor %}
    </ul>
    ...