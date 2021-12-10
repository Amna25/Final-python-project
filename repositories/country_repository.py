from db.run_sql import run_sql

from models.country import Country
from models.city import City

def save(country):
    sql="INSERT INTO countries( name ) VALUES (%s) RETURNING *"
    values = [country.name]
    results = run_sql( sql, values )
    country.id = results[0]['id']
    return country