class Dog:
   
    animal_type = "Mammal"

    def __init__(self, breed, name):
       
        self.breed = breed
        self.name = name



dog1 = Dog("German Shepherd", "Rex")
dog2 = Dog("Labrador", "Buddy")


print("Dog 1:")
print("Name:", dog1.name)
print("Breed:", dog1.breed)
print("Type:", dog1.animal_type)

print() 


print("Dog 2:")
print("Name:", dog2.name)
print("Breed:", dog2.breed)
print("Type:", dog2.animal_type)