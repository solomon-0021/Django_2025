class Car:
    def __init__(self, make):
        self.__make = make

    def get_make(self):
        return self.__make
    


def main():
    car = Car("Tesla")
    print("Car made by:", car.get_make())


if __name__ == "__main__":
    main()