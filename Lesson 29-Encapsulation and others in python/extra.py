class Employee:
    def __init__(self , name , salary):
        self.name=name
        self.__salary=salary


    def setsalary(self):
        print("The name and salary of the person is" , self.name , self.__salary)



e = Employee("Alex" , 1000)
e.setsalary()


