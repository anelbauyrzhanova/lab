#Python dictionaries
#example 1
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

#example 2
#Creating and printing a dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

#example 3
#Printing the "brand" value of the dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

#example 4
#Duplicating values will overwrite existing values:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

#example 5
#Printing the number of items in the dictionary
print(len(thisdict))

#example 6
#String, int, boolean, and list data types:
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

#example 7
#Printing the data type of a dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))

#example 8
#Using the dict() method to make a dictionary:
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

#Access Items
#example 1
#Getting the value of the "model" key:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]

#example 2
#Getting the value of the "model" key:
x = thisdict.get("model")

#example 3
#Getting a list of the keys:
x = thisdict.keys()

#example 4
#When we add a new item to the original dictionary, we can see that the keys list changes as well:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964}
x = car.keys()
print(x) #before the change
car["color"] = "white"
print(x) #after the change

#example 5
#Getting a list of the values:
x = thisdict.values()

#example 6
#by making a change in the original dictionary, we can see that the values list changes as well:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964}
x = car.values()
print(x) #before the change
car["year"] = 2020
print(x) #after the change

#example 7
#Getting a list of the key:value pairs
x = thisdict.items()

#example 8
#Checking if "model" is present in the dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

#Change Values
  
#example 1
#Changing the "year" to 2018:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
#example 2
#Updating the "year" of the car by using the update() method:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

#Adding Items
#example 1
#Adding a color item to the dictionary by using the update() method:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})

#Removing Items
#example 1
#Using the pop() method removes the item with the specified key name:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

#example 2
#Using the popitem() method we remove the last inserted item (in versions before 3.7, a random item is removed instead):
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)
#exanple 3
#The del keyword removes the item with the specified key name:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)
#example 4
#The clear() method empties the dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)

#Loop Dictionaries
#example 1
#Printing all key names in the dictionary, one by one:
for x in thisdict:
  print(x)
#example 2
#Print all values in the dictionary, one by one:
for x in thisdict:
  print(thisdict[x])
#example 3
#Using the values() method to return values of a dictionary:
for x in thisdict.values():
  print(x)
#example 4
#Using the keys() method to return the keys of a dictionary:
for x in thisdict.keys():
  print(x)
#example 5
#Loop through both keys and values, by using the items() method:
for x, y in thisdict.items():
  print(x, y)

#Copy a Dictionary
#example 1
#Making a copy of a dictionary with the copy() method:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)
#example 2
#Making a copy of a dictionary with the dict() function
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

#Nested Dictionaries
#example 1
#Creating a dictionary that contain three dictionaries:
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
#example 2
#creating one dictionary that will contain the other three dictionaries:
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}
myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
#example 3
#Printing the name of child 2:
print(myfamily["child2"]["name"])
