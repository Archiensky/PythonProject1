# === Task 1: Animal, Dog, Cat ===
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sound(self):
        print("The animal makes a sound.")

class Dog(Animal):
    def sound(self):
        print("Woof-woof!")

class Cat(Animal):
    def sound(self):
        print("Meow-meow!")


# === Task 2: Person, Driver ===
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_age(self):
        return self.age

class Driver(Person):
    def __init__(self, name, age, license_number):
        super().__init__(name, age)
        self.license_number = license_number


# === Task 3: Vehicle, Car, Bicycle ===
class Vehicle:
    def __init__(self, speed):
        self.speed = speed

    def move(self):
        print(f"Moving at {self.speed} km/h")

class Car(Vehicle):
    pass

class Bicycle(Vehicle):
    pass


# === Task 4: Device, TV, Laptop ===
class Device:
    def turn_on(self):
        print("Device is turned on")

    def turn_off(self):
        print("Device is turned off")

class TV(Device):
    pass

class Laptop(Device):
    pass


# === Task 5: ProgrammingLanguage, PythonLang, JavaScriptLang ===
class ProgrammingLanguage:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello! I am a programming language called {self.name}.")

class PythonLang(ProgrammingLanguage):
    pass

class JavaScriptLang(ProgrammingLanguage):
    pass


# === Testing all classes ===
if __name__ == "__main__":
    print("\n--- Animals ---")
    dog = Dog("Buddy", 3)
    cat = Cat("Whiskers", 2)
    dog.sound()
    cat.sound()

    print("\n--- Driver ---")
    driver = Driver("John", 35, "AB123456")
    print(f"Name: {driver.name}, Age: {driver.get_age()}, License: {driver.license_number}")

    print("\n--- Vehicles ---")
    car = Car(120)
    bicycle = Bicycle(25)
    car.move()
    bicycle.move()

    print("\n--- Devices ---")
    tv = TV()
    laptop = Laptop()
    tv.turn_on()
    laptop.turn_off()

    print("\n--- Programming Languages ---")
    python = PythonLang("Python")
    javascript = JavaScriptLang("JavaScript")
    python.greet()
    javascript.greet()
