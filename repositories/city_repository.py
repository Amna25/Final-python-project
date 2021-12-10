from db.run_sql import run_sql
from models.city import City
from models.country import Country
import repositories.country_repository as country_repository

def save(country):
    sql= "INSERT INTO countries(name, coutry_id) VALUES(%s, %s)RETURNING id"
    values=