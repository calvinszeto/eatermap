from flask import Flask, render_template, request, jsonify
from flask.ext.sqlalchemy import SQLAlchemy
from locator import Locator

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

class Restaurants(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column('name', db.String)
    address = db.Column('address', db.String, nullable=True)
    website = db.Column('website', db.String, nullable=True)

    def __init__(self, name, address, website):
        self.name = name
        self.address = address
        self.website = website

    def __repr__(self):
        return '<Restaurant %r>' % self.name

@app.route('/_locate_nearest')
def locate_nearest():
    address = request.args.get('address', 'Austin, TX', type=str)
    page = request.args.get('page', 0, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    locator = Locator("./data/geocoded_restaurants.json") 
    curr_location, nearest_locations = locator.nearest(address, page, per_page)
    return jsonify({"loc": curr_location, "results":[location[0] for location in nearest_locations]})

@app.route('/')
def index():
    return render_template('app.html') 

if __name__ == '__main__':
    app.run(debug=True)
