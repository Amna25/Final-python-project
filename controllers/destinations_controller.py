from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.destination import Destination
from models.city import City
import repositories.destination_repository as destination_repository
import repositories.city_repository as city_repository

destinations_blueprint = Blueprint("destinations", __name__)

@destinations_blueprint.route("/destinations")
def destinations():
    destinations = destination_repository.select_all()
    return render_template("destinations/index.html", destinations=destinations)

# NEW
# GET '/destinations/new'
@destinations_blueprint.route("/destinations/new", methods=['GET'])
def new_destination():
    cities = city_repository.select_all()
    return render_template("destinations/new.html", cities = cities)

# CREATE
# POST '/destinations'
@destinations_blueprint.route("/destinations",  methods=['POST'])
def create_destination():
    name = request.form['name']
    city_id = request.form['city_id']
    city = city_repository.select(city_id)
    visited = True if 'visited' in request.form else False
    destination = Destination(name, city, visited)
    destination_repository.save(destination)
    return redirect('/destinations')
    



