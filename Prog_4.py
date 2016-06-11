from faker import Factory
fake = Factory.create("en_US")

for i in range(10):
    print(fake.address())