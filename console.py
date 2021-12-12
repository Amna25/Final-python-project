import pdb

from models.country import Country
from models.city import City
from models.destination import Destination

import repositories.country_repository as country_repository
import repositories.city_repository as city_repository
import repositories.destination_repository as destination_repository


#city_repository.delete_all()
#country_repository.delete_all()

country1= Country('United Kingdom')
country_repository.save(country1)
country2=Country('Pakistan')
country_repository.save(country2)


city1=City("Yest", country1)
city_repository.save(city1)
city2=City("TEst", country1)
city_repository.save(city2)
# city3=City("Big", country2)
#city_repository.save(city3)
# city4=City("Islamabad", country2)
# city_repository.save(city4)
# city5=City("test", country2)
# city_repository.save(city5)

destination1= Destination("Princess Street", city1, True)
destination_repository.save(destination1)
destination2 = Destination("B_Place", city2, False)
destination_repository.save(destination2)



