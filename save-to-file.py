# test
import json


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


jakes_car = Car("Subaru", "XV", "2023")

car_dict = {
    "make": jakes_car.make,
    "model": jakes_car.model,
    "year": jakes_car.year,
}

with open("cars.json", "w") as f:
    json.dump(car_dict, f)

with open("cars.json", "r") as f:
    read_dict = json.load(f)

read_dict = Car(read_dict["make"], read_dict["model"], read_dict["year"])

print(read_dict.make, read_dict.model, read_dict.year)
