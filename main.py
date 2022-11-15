from flask import Flask, render_template, abort
from requests import get

app = Flask(__name__, )

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/hockey")
def hockey():
    return render_template('hockey.html')

if __name__ == '__main__':
    app.run(host="localhost", debug=True, port=9000)