class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


class Owner:
    def __init__(self, name, age, address):
        self.name = name    
        self.age = age    
        self.address = address    

    def info(self):
        vocab = {"name": self.name, "age": self.age, 'address': self.address}   
        return vocab       
                    

class Dog(Animal):
    def __init__(self, nickname, weight, breed, owner):
        self.breed = breed
        self.owner = owner
        super().__init__(nickname, weight)

    def say(self):
        return "Woof"
    def info(self):
        return {
            "nickname": self.nickname,
            "weight": self.weight,
            "breed": self.breed,
            "owner": self.owner.info()
        }

    def who_is_owner(self):
        return self.owner.info()
        
owner = Owner('Graf', 25, 'Lviv')
#print(owner.info())
dog = Dog('Ted', 15, 'labrador', owner)
print(dog.info())