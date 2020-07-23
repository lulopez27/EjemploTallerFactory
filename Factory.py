from abc import ABCMeta, abstractstaticmethod

class Car(metaclass=ABCMeta):
    @abstractstaticmethod
    def getSpecs():
        """All the car specs""";
class FastCar(Car):
    def __init__(self):
        self.doorCount = 2;
        self.maxSpeed = "220 km/h";
        self.accelerationSpeed = "3 s";
    def getSpecs(self):
        return {"No. of doors": self.doorCount,"Max speed": self.maxSpeed,"From 0 to 97 km in ": self.accelerationSpeed}
class SUV(Car):
    def __init__(self):
        self.doorCount = 5;
        self.maxSpeed = "180 km/h";
        self.accelerationSpeed = "13 s";
    def getSpecs(self):
        return {"No. of doors": self.doorCount,"Max speed": self.maxSpeed,"From 0 to 97 km in ": self.accelerationSpeed}
class Hatchback(Car):
    def __init__(self):
        self.doorCount = 2;
        self.maxSpeed = "190 km/h";
        self.accelerationSpeed = "10 s";
    def getSpecs(self):
        return {"No. of doors": self.doorCount,"Max speed": self.maxSpeed,"From 0 to 97 km in ": self.accelerationSpeed}
class CarFactory():
    @staticmethod
    def getCar(carType):
        try:
            if carType=="fast car":
                return FastCar();
            elif carType=="SUV":
                return SUV();
            elif carType=="hatchback":
                return Hatchback();
            raise AssertionError("Car not found");
        except AssertionError as e_:
            print(e_);
if __name__ == "__main__":
    car = CarFactory.getCar("fast car");
    print(car.getSpecs());
    car = CarFactory.getCar("SUV");
    print(car.getSpecs());
    car = CarFactory.getCar("hatchback");
    print(car.getSpecs());
