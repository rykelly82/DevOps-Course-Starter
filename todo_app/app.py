from flask import Flask, render_template, redirect, request

from todo_app.flask_config import Config
from todo_app.data.trello_items import add_item, get_items

app = Flask(__name__)
app.config.from_object(Config())

@app.route('/')
def index():
    items = get_items()
    return render_template('index.html', items = items)

@app.route('/add_todo_item', methods = ['POST'])
def add_todo():
    new_todo_title = request.form.get('title')
    add_item(new_todo_title)
    return redirect('/')