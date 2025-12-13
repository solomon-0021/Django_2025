class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
    
    def info(self):
        print(f"Car brand: {self.brand}")
        print(f"Year of release: {self.year}")


class Car(Vehicle):
    def __init__(self, brand, year, model):
        super().__init__(brand, year)
        self.model = model
    def info(self):
        print(f"Brand: {self.brand} Model: {self.model} Year: {self.year}")


def main():
    vehicle = Vehicle("Toyota", 2020)
    car = Car(year=2025, model="tl-25", brand="Tesla")

    vehicle.info()
    car.info()


if __name__ == "__main__":
    main()
    