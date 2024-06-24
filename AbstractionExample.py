from abc import ABC, abstractmethod

class Car(ABC):
    def Show(self):
        print("Every Car has 4 Wheels")
    @abstractmethod
    def Speed(self):
        pass
class Maruti(Car):
    def Speed(self):
        print("Speed is 100Km/H")

class Suzuki(Car):
    def Speed(self):
        print("Speed is 70Km/H")

obj = Maruti()
obj.Show()
obj.Speed()

obj2 = Suzuki()
obj2.Show()
obj2.Speed()