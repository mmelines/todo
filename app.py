from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost:5432/todos'
db = SQLAlchemy(app)

class Person(db.Model):
    __tablename__ = 'persons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'Person ({self.id}): {self.name}'

class Todo(db.Model):
    __tablename__ = 'todo'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'#{self.id}. {self.description}'

db.create_all()

@app.route('/')
def index():
    data = Todo.query.order_by(Todo.id.desc()).all()
    return render_template('pages/index.html', data=data)

@app.route('/todos/create', methods=["GET"])
def new_todo():
    return render_template('pages/new_item.html')

@app.route('/todos/create', methods=["POST"])
def submit_new_todo():
    description = request.form.get('description')
    todo =  Todo(description=description)
    try:
        db.session.add(todo)
        db.session.commit()
    except:
        db.session.rollback()
    finally:
        return redirect(url_for('index'))

if __name__=='__main__':
    app.run(port=5001)