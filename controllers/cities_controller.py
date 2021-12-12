from flask import Flask,render_template,request,redirect
from flask import Blueprint
from models.city import City
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

cities_blueprint = Blueprint("cities", __name__)

@cities_blueprint.route("/cities")
def cities():
    cities = city_repository.select_all()
    return render_template("cities/index.html", cities=cities)

# SHOW
@cities_blueprint.route("/cities/<id>")
def show_city(id):
    city = city_repository.select(id)
    return render_template("cities/show.html", city=city)


#New
#GET '/cities/new'
@cities_blueprint.route("/cities/new", methods=['GET'])
def new_city():
    countries= country_repository.select_all()
    return render_template("cities/new.html", countries=countries)

    
#POST '/cities'
@cities_blueprint.route("/cities", methods=['POST'])
def create_city():
    name = request.form['name']
    country_id = request.form['country_id']
    country = country_repository.select(country_id)
    new_city=City(name, country)
    city = City(name,country)
    city_repository.save(new_city)
    return redirect('/cities')

#DELETE
#DELETE '/cities/<id>'
@cities_blueprint.route("/cities/<id>/delete", methods=['POST'])
def delete_city(id):
    city_repository.delete(id)
    return redirect('/cities')
