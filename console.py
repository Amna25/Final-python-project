import pdb
from models.country import Country

import repositories.country_repository as country_repository

country1= Country('United Kingdom')
country_repository.save(country1)
country2=Country('Pakistan')
country_repository.save(country2)