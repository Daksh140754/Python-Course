from abc import ABC , abstractmethod
class ABSmethod(ABC):

    def print(self , X):
        print("Passed value:" , X)


    @abstractmethod
    def task(self):
        print("We are inside abstract class")



class test_class(ABSmethod):
    def task(self):
        print("We are inside test_class task")


test_obj=test_class()
test_obj.task()
test_obj.print(100)





