def add(n1,n2):
    print("n1 :",n1)
    print("n2 :",n2)
    print("n1+n2 :",n1+n2)

## postional arguments
# This is use to pass the arguments in sequence
# order  matter
add(1,2)

## Keyword argruments
# order does not matters
# This is used to pass arguments by name
add(n1=1,n2=3)
add(n2=2,n1=2)

# vairable length arguments
def show_vairable_length(*args):
    print("vairable length is",len(args))
    
show_vairable_length(3,2,4,2)

## Nested functions

def output_function():
    x=1
    
    def inner_function():
        y=2
        result=x+y
        return result
    
    return inner_function()
output=output_function()

print(output)

'''
Python’s argument-passing model is neither “Pass by Value” nor “Pass by Reference” but it is “Pass by Object Reference”. 

Depending on the type of object you pass in the function, the function behaves differently. Immutable objects show “pass by value” whereas mutable objects show “pass by reference”. '''

## Pass by Value : change in formal parameter not reflected to actual parameters
# Integers are immutable objects hence Python works according to call by value, and the changes made in the function are not reflected outside the function.

def passByValue(a):
    a=a*10
    print(a)
  
a=5  
passByValue(a)
print(a)

## Pass by refrence : change in formal parameter  reflected to actual parameters

# We use mutable objects for this like list, dictionary etc...

def passByRefrence(lst):
    lst.append(10)
    print(lst)
  
lst=[1,3,4]
passByRefrence(lst)
print(lst)







