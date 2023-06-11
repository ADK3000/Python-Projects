from faker import Faker 

fake=Faker(['en_IN'])

print('Phone Number:',fake.phone_number())
print('Country ccalling code:',fake.country_calling_code())
print('MSISDN:',fake.msisdn())