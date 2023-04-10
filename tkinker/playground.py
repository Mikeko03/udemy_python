

def add(*args):
    return sum(args)
#
#print(add(4,5,6,3,2,2))
#print(add(2,2))
#
#print(add(4,5,6,2))
#
class Car():

    def __init__(self, **kwargs):
        self.model = kwargs.get("model")
        self.maker = kwargs.get("maker")
        self.seats = kwargs.get("seats")


car = Car(model = "Cee'd",maker = "Kia" ,seats = 4)

print(car.model)
print(car.maker)
print(car.seats)
