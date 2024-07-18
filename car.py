# car class

class car:
    # constructor
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
    # print attributes dunder method
    def __str__(self):
        return f"The {self.color} car has {self.mileage} miles"

if __name__ == "__main__":
    
    my_blue_car = car("blue", 20000)
    my_red_car = car("red", 30000)
    
    print(my_blue_car)
    print(my_red_car)