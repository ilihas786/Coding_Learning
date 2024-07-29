
class BaseClass:
    # Base class (superclass) definition
    def __init__(self):
        self.base_attribute = "I am from BaseClass"
    
    def base_method(self):
        print("Method in BaseClass")

class DerivedClass(BaseClass):
    # Derived class (subclass) definition
    def __init__(self):
        super().__init__()  # Call the constructor of the superclass
        self.derived_attribute = "I am from DerivedClass"
    
    def derived_method(self):
        print("Method in DerivedClass")
        print("base attribute :",self.base_attribute)
        print("derived attribute :",self.derived_attribute)
        
obj=DerivedClass()
obj.derived_method()

'''
output :
Method in DerivedClass
base attribute : I am from BaseClass      
derived attribute : I am from DerivedClass
'''

# Single inheritance " mention above "

# multipe inheritance 
class Engine:
    def start(self):
        print("Engine started")

    def stop(self):
        print("Engine stopped")

class Wheels:
    def roll(self):
        print("Wheels are rolling")

class Vehicle(Engine, Wheels):
    def __init__(self, name):
        self.name = name

    def drive(self):
        self.start()
        self.roll()
        print(f"Driving {self.name}")
        self.stop()

# Using the multiple inheritance
car = Vehicle("Car")

car.drive()

# Output:
# Engine started
# Wheels are rolling
# Driving Car
# Engine stopped


# multilevel inheritance 

class LivingBeing:
    def __init__(self):
        print("LivingBeing is initialized")

    def breathe(self):
        print("Breathing")

class Animal(LivingBeing):
    def __init__(self):
        super().__init__()
        print("Animal is initialized")

    def eat(self):
        print("Eating")

class Mammal(Animal):
    def __init__(self):
        super().__init__()
        print("Mammal is initialized")

    def walk(self):
        print("Walking")

# Using the multilevel inheritance
mammal = Mammal()

mammal.breathe()  # Inherited from LivingBeing
mammal.eat()      # Inherited from Animal
mammal.walk()     # Defined in Mammal

# hierarchical inheritance 

'''
Hierarchical inheritance occurs when multiple subclasses inherit from a single parent class. This type of inheritance allows you to create different types of objects that share common functionality from a base class but have their own specific behaviors.
'''

class Animal:
    def __init__(self, name):
        self.name = name

    def breathe(self):
        print(f"{self.name} is breathing")

class Bird(Animal):
    def fly(self):
        print(f"{self.name} is flying")

class Fish(Animal):
    def swim(self):
        print(f"{self.name} is swimming")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking")

# Using the hierarchical inheritance
sparrow = Bird("Sparrow")
goldfish = Fish("Goldfish")
bulldog = Dog("Bulldog")

sparrow.breathe()  # Inherited from Animal
sparrow.fly()      # Defined in Bird

goldfish.breathe() # Inherited from Animal
goldfish.swim()    # Defined in Fish

bulldog.breathe()  # Inherited from Animal
bulldog.bark()     # Defined in Dog
