from faker import Faker

fake=Faker(['en_US'])

print('Job post:',fake.job())
print('Company Name:', fake.company())
print('Company Slogan', fake.bs())
print('Company Phrase:', fake.catch_phrase())
print('Company Suffix', fake.company_suffix())