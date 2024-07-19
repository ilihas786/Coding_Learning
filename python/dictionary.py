# elements are ordered
# mutable
# unindexed but accessable through the key
# mixed data type

# creating the dictionary
phones={
    "john":12345,
    "Ria":67890
}

print(phones)

# check the length of the dictionary
print(len(phones))

# acess the items of dictionary
print(phones["john"])
print(phones.get("Ria"))

# print the all of the keys
print(phones.keys())

# update the value of the dictionary
phones["john"]=94949494

# add the elements to the dictionary
phones["Kia"]=95437
print(phones)

# add the another dictionary
more_phones={
    "Tia":959220
}
phones.update(more_phones)
print(phones)

# remove the elements from the dictionary
phones.pop("Ria")
print(phones)

# remove the last element from the dictionary
phones.popitem()

# to empty the dictionary
phones.clear()

# looping the keys of dictionary
for x in phones:
    print(x)
    
# looping the values of dictionary
for x in phones:
    print(phones[x])

# looping through both key and value in pairs
for x in phones.items():
    print(x)

#looping througth the key and values seperately
for x,y in phones.items():
    print("key : ",x)
    print("value : ",y)
    

# nested dictionary

dict={
    "area1":{
        "x":0,
        "y":1
    },
    "area2":{
        x:"2",
        y:"3"
    }
    
}

print(dict)

# accesing the nested dictionary
print(dict["area1"]["x"])