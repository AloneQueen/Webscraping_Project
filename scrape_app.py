#!/usr/bin/env python

from flask import Flask, json, render_template, request
from scrape_func import craigslist_scrape
import os

#create instance of Flask app
app = Flask(__name__)

#decorator
@app.route("/")
def echo_hello():
    return render_template('intro.html')
    #add more info about how to use 

@app.route("/scrape")
def scrape():

    func_output = craigslist_scrape()

    return render_template('index.html', data=func_output)

# @app.route("/scrape/all")
# def all():
#     json_url = os.path.join(app.static_folder,"","us_gdp.json")
#     data_json = json.load(open(json_url))

#     data = data_json[1]
#     #print(data)
#     year = request.view_args['year']

#     output_data = [x for x in data if x['date']==year]
#     return render_template('index.html',data=output_data)

if __name__ == "__main__":
    app.run(debug=True)


## GitBash
## export FLASK_APP=scrape_app
## flask run