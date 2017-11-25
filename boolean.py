from faker import Faker
fake = Faker()

fake.name()

for _ in range(10):
    print(fake.name())
    print (fake.address())

for _ in range(4):
    print (fake.address())
#'Lucy Cechtelar'

#username = "admin"
#password = "hoid"

# if username == "admin" and password == "admin123":
#     print("Valid user")
# else:
#         print("Invalid user")