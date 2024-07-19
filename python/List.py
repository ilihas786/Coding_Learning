## list can hold multiple data types

a=[1,"one",True]
print(a)

## list element access

list=[-1,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

print(list[2]) # print entered index element 
print(list[-2]) # print the entered index element from last

# print the element in range 
# syntax list[start:end] print elements from start to end-1

print(list[2:5])
print(list[-3:-1])

## methods in list
list.append(3) # add element to end of the list
list.extend([2,3,4,5]) # add list to new list
print(list)

list.remove(3) # remove element (all occurence)  from list
print(list)
list.pop() # remove the last element

## List comprehension 
# here we add the condtions in small format to form new list from existing list
newlist=[i for i in list if i>5]
print(newlist)
