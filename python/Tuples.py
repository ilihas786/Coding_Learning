# Tuples values are not changed (immutable)
tuple=("one","two","three","four","five","six")

# tuple with one element should be have , after one element
fruit=("apple",) # this is tuple
print(fruit)
fruit=("apple") # this is not tuple, it is just a simple vairable 
print(fruit)

## Accessing elements in tuples
print(tuple[0])
# others method same as list

## checking the elements in the tuple
three="three"
if three in tuple:
    print("Three is in the tuple")
    
## tuple destructring
newtuple=(1,3,4)
a,b,c=newtuple
print(a,b,c)

# this code will give error as there are not sufficient element to unpack
# a,c=newtuple
# print(a,c)


# this code will give error as there are more than sufficient element to unpack
# a,b,c,d=newtuple
# print(a,b,c,d)

## iterating the tuples in reverse order

for i in reversed(tuple):
    print(i)


    
