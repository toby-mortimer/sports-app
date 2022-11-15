from flask import Flask, render_template, abort
from requests import get

app = Flask(__name__, )

@app.route("/")
def index():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(host="localhost", debug=True, port=9000)