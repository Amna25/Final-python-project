from flask import Flask, render_template,request,redirect
from flask import Blueprint
from models.country import Country
import repositories.country_repository as country_repository
import repositories.city_repository as city_repository
countries_blueprint = Blueprint("countries", __name__)

@countries_blueprint.route("/countries")
def countries ():
    countries = country_repository.select_all()
    return render_template("countries/index.html", countries = countries)

@countries_blueprint.route("/countries/<id>")
def show(id):
    country = country_repository.select(id)
    cities = country_repository.cities(country)
    return render_template("countries/show.html", country=country, cities=cities)


#New
#GET '/countries/new
@countries_blueprint.route("/countries/new", methods=['GET'])
def new_country():
    cities=city_repository.select_all()
    return render_template("countries/new.html", cities=cities)


#Create
#Post '/countries'
@countries_blueprint.route("/countries", methods=['POST'])
def create_country():
    name = request.form['name']
    country = Country(name)
    country_repository.save(country)
    return redirect('/countries')
