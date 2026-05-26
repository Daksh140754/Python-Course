class Vehicle:

    def __init__(self , max_speed  , mileage):
        
        self.max_speed= max_speed
        self.mileage = mileage


ModelX=Vehicle(350 , 20)

print("Maximum speed of the car is:" , ModelX.max_speed)
print("Mileage of the car is:" , ModelX.mileage)
        