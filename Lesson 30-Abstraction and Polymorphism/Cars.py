class BMW():
    def fuel_type(self):
        print("BMW operates or runs on petrol")

    def top_speed(self):
        print("The top speed of BMW is 300km/h ")

    
class Ferrari():
    def fuel_type(self):
        print("Ferrari runs either on CNG or normal fuel")

    def top_speed(self):
        print("The top speed of Ferrari is 360km/h")

obj_BMW=BMW()
obj_Ferrari=Ferrari()

for cars in (obj_BMW , obj_Ferrari):
    cars.fuel_type()
    cars.top_speed()
        

    