class Vehicle:
    def __init__ (self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def print_info(self):
        return "the car is a {} {} from {}".format (self.make, self.model, self.year)
    
car = Vehicle("nissan ", "leaf ", "2015 ")
# print (car.make, car.model, car.year)
print(car.print_info())

