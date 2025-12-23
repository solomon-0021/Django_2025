from abc import ABC, abstractmethod


class Appliance(ABC):
    @abstractmethod
    def turn_on(sel):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class WashingMachine(Appliance):
    def __init__(self):
        pass

    def turn_on(self):
        print("Washing machine turned on")

    def turn_off(self):
        print("Washing machine turned off")

def main():
    machine = WashingMachine()
    machine.turn_on()
    machine.turn_off()

if __name__ == "__main__":
    main()