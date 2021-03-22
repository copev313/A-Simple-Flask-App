# app.py

from flask import Flask, render_template

# Create the application instance:
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')


# Start our server:
if __name__ == '__main__':
    app.run()

# `flask run --host=0.0.0.0` will make site publicly available to your network.
