from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost:5432/todos'
db = SQLAlchemy(app)

@app.route('/')
def index():
    return 'Hello World'

if __name__=='__main__':
    app.run(port=5001)