class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print("Animal makes sound.")


class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        print("Meow Meow!")


def main():

    cat = Cat("Joy", 3)
    animal = Animal("None", 0)
    print(f"Cat Name: {cat.name}")
    print(f"Cat Age: {cat.age}")

    print("Animal sound")
    animal.make_sound()
    print("Cat sound")
    cat.make_sound()


if __name__ == "__main__":
    main()
