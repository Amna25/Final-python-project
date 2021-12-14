from db.run_sql  import run_sql
from models import destination
from models.destination import Destination
from models.city import City

import repositories.city_repository as city_repository

def save(destination):
    sql= "INSERT INTO destinations (name,city_id,visited) VALUES(%s, %s, %s)RETURNING *"
    values = [destination.name, destination.city.id, destination.visited]
    results = run_sql(sql, values)
    id = results[0]['id']
    destination.id = id
    return destination

def select_all():
    destinations = []
    sql = "SELECT * FROM destinations"
    results = run_sql(sql)

    for row in results:
        city = city_repository.select(row['city_id'])
        destination = Destination(row['name'], city, row['visited'], row['id'])
        destinations.append(destination)
    return destinations

def select(id):
    destination = None
    sql = "SELECT * FROM destinations WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        city =city_repository.select(result['city_id'])
        destination = destination(result['name'], city, result['visited'], result['id'] )
    return destination

def delete_all():
    sql = "DELETE  FROM destinations"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM destinations WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(destination):
    sql = "UPDATE destinations SET (name, city_id, visited) = (%s, %s, %s) WHERE id = %s"
    values = [destination.name, destination.city.id, destination.visited, destination.id]
    run_sql(sql, values)

def cities(destination):
    cities = []

    sql= "SELECT * FROM cities WHERE destination_id = %s"
    values = [destination.id]
    results = run_sql(sql, values)
    for row in results:
        city= City(row['name'], row['visited'], row['country.id'],row['id'])
        cities.append(city)
    return cities

def select_all_visited():
    destinations = []
    sql = "SELECT * FROM destinations WHERE visited = True"
    results = run_sql(sql)
    for row in results:
        city = city_repository.select(row['city_id'])
        destination = Destination(row['name'], city, row['visited'], row['id'])
        destinations.append(destination)
    return destinations

def select_all_still_to_visit():
    destinations = []
    sql = "SELECT * FROM destinations WHERE visited = False"
    results = run_sql(sql)
    for row in results:
        city = city_repository.select(row['city_id'])
        destination = Destination(row['name'], city, row['visited'], row['id'])
        destinations.append(destination)
    return destinations

# def search_for_destinations(cities):
#     cities = []
#     sql = "SELECT * FROM cities WHERE destination_id=%s"
#     values = [destination.id]
#     results = run_sql(sql, values)
#     for row in results:
#         city= City(row['name'],row['country.id'],row['id'])
#         cities.append(city)
#     return cities
    