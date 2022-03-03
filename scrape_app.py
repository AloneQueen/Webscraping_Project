#!/usr/bin/env python

from flask import Flask, render_template
from scrape_func import craigslist_scrape
from IPython.display import HTML

#create instance of Flask app
app = Flask(__name__)

url, df = craigslist_scrape()
html_table = HTML(df.to_html(justify="center", classes="table table-striped", index=False))

#decorator
@app.route("/")
def welcome():
    return render_template('intro.html')

@app.route("/scrape")
def scrape():
    return render_template('index.html', data=url)

@app.route("/scrape/all")
def all():
    return render_template('index.html', data=html_table)

if __name__ == "__main__":
    app.run(debug=True)


## GitBash
## export FLASK_APP=scrape_app
## flask run