from flask import Flask,render_template,request,redirecct
from flask import Blueprint
from werkzeug.utils import redirect
from models.city import City
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

cities_blueprint = Blueprint("cities", __name__)

@cities_blueprint.route("/cities")
def cities():
    cities = city_repository.select_all()
    return render_template("cities/index.html", cities=cities)

#New
#GET '/cities/new'
@cities_blueprint.route("/cities/new", methods=['GET'])
def new_city():
    countries = country_repository.select_all()
    return render_template("cities/new.html" ,countries=countries)

#CREATE
#POST '/cities'
@cities_blueprint.route("/cities", methods=['POST'])
def create_city():
    name = request.form['name']
    country_id = request.form['country_id']
    country = country_repository.select(country_id)
    city = City(name,country)
    city_repository.save(city)
    return redirect('/cities')

#DELETE
#DELETE '/cities/<id>'
@cities_blueprint.route("/cities/<id>/delete", methods=['POST'])
def delete_city(id):
    city_repository.delete(id)
    return redirect('/cities')
