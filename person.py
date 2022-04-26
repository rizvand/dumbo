from faker import Faker
fake = Faker()

class RandomPerson():
    def __init__(self):
        self.name = fake.name()
        self.address = fake.address()
    
    def identity(self):
        return {
            "name": self.name,
            "address": self.address
        }