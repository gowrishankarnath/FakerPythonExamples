from faker import Factory
fake = Factory.create("hi_IN")
print(fake.name())