#Examples
#Tuple - ordered, unchangeable, allow duplicates

#example 1
#Creating a tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#example 2
#Print the number of items in the tuple
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#example 3
#commas are important
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")

#example 4
#A tuple can contain different data types
tuple1 = ("abc", 34, True, 40, "male")

#example 5
#Using the tuple() method to make a tuple
thistuple = tuple(("apple", "banana", "cherry")) 
print(thistuple)

#Access Tuple Items
#example 1
#Printing the second item in the tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#example 2
#Printing the last item of the tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

#example 3
#returning the items from index -4 (included) to index -1 (excluded)
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

#example 4
#Checking if "apple" is present in the tuple
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

#Update Tuples
#example 1
#Converting the tuple into a list to be able to change it
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

#example 2
#Converting the tuple into a list, add "orange", and convert it back into a tuple
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

#example 3
#Creating a new tuple with the value "orange", and add that tuple
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

#example 4
#Converting the tuple into a list, remove "apple", and convert it back into a tuple
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

#example 5
#The del keyword can delete the tuple completely
thistuple = ("apple", "banana", "cherry")
del thistuple
#print(thhistuple) will give an error because tuple no longer exists

#Unpack Tuples
#example 1
#Packing a tuple
fruits = ("apple", "banana", "cherry")

#example 2
#Unpacking a tuple
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

#example 3
#Assigning the rest of the values as a list called "red"
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

#example 4
#Adding a list of values the "tropic" variable
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

#Loop Through a Tuple
#example 1
#Print all items by referring to their index number
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

#example 2
#Print all items, using a while loop
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1


#Join Tuples
#example 1
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

#example 2
#Multiply Tuples
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)


