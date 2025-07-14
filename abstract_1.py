from abc import ABC,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def litre(self):
        pass
class bike(Vehicle):
    def litre(self):
        print("420")
obj=bike()
obj.litre()
    