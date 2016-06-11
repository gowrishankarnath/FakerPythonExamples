from faker import Factory
fake = Factory.create()

for i in range(10):
    print(fake.currency_code())