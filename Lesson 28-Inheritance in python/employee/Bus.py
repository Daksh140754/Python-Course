class Vehicle:

    def __init__(self , seating_capacity):
        self.seating_capacity= seating_capacity
        self.fare = seating_capacity*100


class Bus(Vehicle):
    def __init__(self , seating_capacity):
        super().__init__(seating_capacity)
        self.fare = self.seating_capacity*100


my_bus = Bus(seating_capacity=50)
print("Total fare for the bus is:"  ,my_bus.fare)




    