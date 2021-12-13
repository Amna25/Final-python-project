from flask import Flask, render_template,redirect,request
from flask import Blueprint
from models.country import Country
import repositories.country_repository as country_repository

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
    return render_template("countries/new.html")


#Create
#Post '/countries'
@countries_blueprint.route("/countries", methods=["POST"])
def create_country():
    name = request.form["name"]
    visited = True if 'visited' in request.form else False
    new_country = Country(name,visited)
    country_repository.save(new_country)
    return redirect("/countries")

#EDIT
@countries_blueprint.route("/countries/<id>/edit")
def edit_country(id):
    country = country_repository.select(id)
    return render_template('countries/edit.html', country=country)

#UPDATE
@countries_blueprint.route("/countries/<id>", methods=["POST"])
def update_country(id):
    name = request.form["name"]
    visited=True if 'visited' in request.form else False
    country = Country(name,visited, id)
    country_repository.update(country)
    return redirect("/countries")

#DELETE
@countries_blueprint.route("/countries/<id>/delete", methods=["POST"])
def delete_country(id):
    country_repository.delete(id)
    return redirect("/countries")

# SHOW
@countries_blueprint.route("/countries/visited")
def show_visited_countries():
    countries = country_repository.select_all_visited()
    return render_template("destinations/visit.html", countries=countries )

#still_to_visited
@countries_blueprint.route("/countries/not_visited")
def show_not_visited_countries():
    countries = country_repository.select_all_still_to_visit()
    return render_template("destinations/not_visit.html", countries=countries )
