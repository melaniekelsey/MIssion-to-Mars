## Using flask to open a template and go to a website and create a website
from flask import Flask, render_template, redirect, url_for
## Using pymongo to work with Mongo DB
from flask_pymongo import PyMongo
## Scraping down we will convert from Jupyter notebook to Python
import scraping
## Sets up flask
app = Flask(__name__)
# Use flask_pymongo to set up mongo connection, using a URI to connect
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)
#App Routes
#Main route - shows homepage
@app.route("/")
#Uses pymongo to find the mars collection in our db and assign that path to the mars variable
#return render_temple tells Falsk to return an HTML template using an index.html file
def index():
   mars = mongo.db.mars.find_one()
   return render_template("index.html", mars=mars)
#Scraping route
#Button of our web application
#mars = tells us where to get the data in Mongodb
#New variable that hosts the scrpated data
#updates the data and putting it in an JSON file
#Last line redirects to see the updated content
@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = scraping.scrape_all()
   mars.update({}, mars_data, upsert=True)
   return redirect('/', code=302)
#Tells flask to run the script
if __name__ == "__main__":
   app.run()