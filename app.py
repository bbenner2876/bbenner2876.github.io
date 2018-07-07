#Run with python app.py

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hello')
def hello():
    return render_template('hello.html')


@app.route('/hidden')
def hidden():
    return "You found the hidden page!"


if __name__ == '__main__':
    app.run(debug=True)
