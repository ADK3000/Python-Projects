from faker import Faker

fake=Faker(['en_IN'])

print('My Address:', fake.address())
print('Building Number:', fake.building_number())
print('City Name:', fake.city_name())
print('Street Name:', fake.street_name())
print('Street suffix:', fake.street_suffix())
print('Country Name:', fake.country())
print('Country Code:', fake.country_code())
print('Current Country Name:', fake.current_country())
print('Current Country Code:', fake.current_country_code())
print('Postcode:', fake.postcode())
print('Zipcode:', fake.zipcode())
print('State:', fake.adminstrative_unit())
print('Latitude and Longitude:', fake.latitude(), fake.longitude())