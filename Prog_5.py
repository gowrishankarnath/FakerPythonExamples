from faker import Factory
fake = Factory.create("en_US")

print(fake.last_name_male())

print(fake.name_female())

print(fake.prefix_male())

print(fake.prefix())

print(fake.name())

print(fake.suffix_female())

print(fake.name_male())

print(fake.first_name())

print(fake.suffix_male())

print(fake.suffix())

print(fake.first_name_male())

print(fake.first_name_female())

print(fake.last_name_female())

print(fake.last_name())

print(fake.prefix_female())