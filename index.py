from cgitb import html
from html.entities import html5
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('/LOGIN/login.html')

@app.route('/about')
def about():
    return render_template('/LOGIN/about.html')

if __name__ == '__main__':
    app.run(debug=True)

