#Run with python app.py

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ucsd')
def ucsd():
    return render_template('ucsd.html')


@app.route('/veritone')
def veritone():
    return render_template('ucsd.html')


@app.route('/climatelens')
def climatelens():
    return render_template('climatelens.html')


@app.route('/tomo')
def tomo():
    return render_template('tomo.html')


if __name__ == '__main__':
    app.run(debug=True)
