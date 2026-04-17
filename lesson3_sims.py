import random
class Human:
    def __init__(self, name="Human", job=None, home=None, car=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.car = car
        self.home = home

    def get_home(self):
        pass

    def get_car(self):
        pass

    def get_job(self):
        pass


class Car:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumtion = brand_list[self.brand]["consumtion"]


brands_of_car = {
    "BMW": {"fuel": 100, "strength": 100, "consumtion": 6},
    "Farrari": {"fuel": 200, "strength": 500, "consumtion": 10},
    "Lamborgihni": {"fuel": 200, "strength": 500, "consumtion": 9},
    "Bugati": {"fuel": 230, "strength": 1000, "consumtion": 10}
}