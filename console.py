import pdb

from models.city import City
from models.country import Country

import repositories.city_repository as city_repository
import repositories.country_repository as country_repository


country1= Country('United Kingdom')
country_repository.save(country1)
country2=Country('Pakistan')
country_repository.save(country2)


city1=City("Edinburgh", country1)
city_repository.save(city1)
city2=City("Glasgow", country1)
city_repository.save(city2)
city3=City("Lahore", country2)
city_repository.save(city3)
city4=City("Islamabad", country2)
city_repository.save(city4)