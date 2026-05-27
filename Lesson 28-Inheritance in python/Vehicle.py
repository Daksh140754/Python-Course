class Vehicle:

    def __init__(self , name , speed , mileage):
        self.name= name
        self.speed = speed
        self.mileage = mileage



class Bus(Vehicle):
    pass

school_bus = Bus("School Volvo" , 200 , 15)
print("Vehicle name:" , school_bus.name , "Speed of the vehicle:" , school_bus.speed ,  "Mileage of the vehicle:" , school_bus.mileage)