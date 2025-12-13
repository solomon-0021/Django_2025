class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hello, {self.name}")
    



def main():
    person = Person("John", 10)

    print(f"Name: {person.name}")
    print(f"Age: {person.age}")
    person.greet()

if __name__ == "__main__":
    main()