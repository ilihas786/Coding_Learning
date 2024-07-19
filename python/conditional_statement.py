## match case

a=10

# This is same as the Swith statement
match a:
    case 1:
        print("one")
    case 2:
        print("two")
    case _: # default case
        print("default")
        
## ternary operator
b="ten" if a==10 else "not ten"
print(b)
