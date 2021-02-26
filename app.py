# app.py

from flask import Flask, render_template

# Create the application instance:
app = Flask(__name__)


# We utilize decorators to link our function to a URL.
@app.route('/')
def home():
    # Return a string:
    return render_template('home.html')


@app.route('/welcome')
def welcome():
    # Render a template:
    return render_template('welcome.html')


# Start our server:
if __name__ == '__main__':
    app.run(debug=True)

# `python app.py` to run site.
# `flask run --host=0.0.0.0` will make site publicly available to your network.
