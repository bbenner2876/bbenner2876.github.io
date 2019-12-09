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
    return render_template('veritone.html')


@app.route('/climatelens')
def climatelens():
    return render_template('climatelens.html')


@app.route('/tomo')
def tomo():
    return render_template('tomo.html')

@app.route('/hvac')
def hvac():
    return render_template('hvac.html')

@app.route('/redesign')
def redesign():
    return render_template('https://www.figma.com/proto/LbFcsGD4sd4vZgo5qHFVj8/parking-REDESIGN?node-id=83%3A3&scaling=scale-down')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')




if __name__ == '__main__':
    app.run(debug=True)
