# items in set are unordered means arrange item in random order on every time we excute the set
# cannot access item by indexes
# immutable
# duplicates are not allowed
# mix different data types

# Creating the set

names={"Sia","Mia"}
print(names)

# check the length
print(len(names))

#acess the item in set

for x in names:
    print(x)
    
# check if the item in set

if "Sia" in names:
    print("present")
    
# add the item to the set
names.add("ilihas")
print(names)

# add the  sequence of elements to the set
names_list=['Chandu',"susu"]
names.update(names_list)
print(names)

# remove the item from the set
# it throws error if element is not found
names.remove("ilihas")
print(names)

# to deal with that error we use discard function
names.discard("ilihas")
print(names)

# join/union the two sets together
s1={1,2,3}
s2={4,5,6}
s3=s1.union(s2)
print(s3)

# keep only duplicates / intersection
s1.intersection_update(s2)
print(s1)

# minus operation
s1.symmetric_difference_update(s2)
print(s1)
