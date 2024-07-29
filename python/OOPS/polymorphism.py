class Animal:
    def make_sound(self):
        # Define a general sound method
        print("Some generic animal sound")

class Dog(Animal):
    def make_sound(self):
        # Override to provide specific implementation
        print("Woof! Woof!")

class Cat(Animal):
    def make_sound(self):
        # Override to provide specific implementation
        print("Meow! Meow!")

class Cow(Animal):
    def make_sound(self):
        # Override to provide specific implementation
        print("Moo! Moo!")

# Function to demonstrate polymorphism
def animal_sound(animal):
    # Calls the make_sound method of the passed animal
    animal.make_sound()

# Using polymorphism
dog = Dog()
cat = Cat()
cow = Cow()

animal_sound(dog)  # Output: Woof! Woof!
animal_sound(cat)  # Output: Meow! Meow!
animal_sound(cow)  # Output: Moo! Moo!


# Compile Time Polymorphism

# Run time polymorphism