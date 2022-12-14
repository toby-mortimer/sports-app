from flask import Flask, render_template, abort
from requests import get

app = Flask(__name__, )

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/hockey")
def hockey():
    return render_template('hockey.html')

@app.route("/hockey/news")
def hockey_news():
    return render_template('hockey_news.html')

@app.route("/hockey/highlights")
def hockey_highlights():
    return render_template('hockey_highlights.html')

@app.route("/hockey/standings")
def hockey_standings():
    return render_template('hockey_standings.html')

@app.route("/boxing")
def boxing():
    return render_template('boxing.html')

@app.route("/netball")
def netball():
    return render_template('netball.html')

@app.route("/formula1")
def formula1():
    return render_template('formula1.html')

@app.route("/wseries")
def wseries():
    return render_template('wseries.html')

@app.route("/football")
def football():
    return render_template('football.html')

@app.route("/tennis")
def tennis():
    return render_template('tennis.html')

if __name__ == '__main__':
    app.run(host="localhost", debug=True, port=9000)