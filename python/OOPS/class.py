'''In C++, class member variables are typically defined before the methods because the compiler needs to know the layout of the class before generating code for its methods. This requirement stems from the need for a clear definition of the memory layout of an object, which includes understanding the size and type of its member variables.

In Python, the situation is different due to its dynamic nature. Here are a few reasons why you don't need to define class attributes before methods in Python:

    Dynamic Typing: Python is dynamically typed, meaning that you don't have to declare the type of a variable before using it. This allows you to define attributes anywhere in the class, usually within the __init__ method or even outside of it.

    Interpreter vs. Compiler: Python is an interpreted language, so there isn't a compilation step that requires knowledge of the complete class layout before using its methods. Python's interpreter handles variable definitions dynamically at runtime.

    Flexibility: Python allows for the dynamic creation of attributes, meaning you can add new attributes to instances of classes even outside the class definition. This is not typically allowed in statically typed languages like C++.

    Readability and Organization: Defining attributes within the __init__ method or as needed helps with code readability and organization. It clearly shows where and how each attribute is intended to be used.'''

class student:
    def set_name(self,name):
        self.name = name
        
    def get_name(self):
        return self.name
    
student1=student()
student1.set_name('ilihas')
print(student1.get_name())
