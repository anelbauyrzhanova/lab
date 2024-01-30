#Examples
#Python Lists

#example 1
#creating a list
thislist = ["apple", "banana", "cherry"]
print(thislist)

#example 2
#list allows duplicate values
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#example 3
#Print the number of items in the list:
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#example 4
#A list can contain different data types:
list1 = ["abc", 34, True, 40, "male"]

#example 5
#What is the data type of a list?
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

#example 6
#Using the "list()" constructor to make a List:
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

#Access List Items

#example 1
#Printing the second item of the list
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#example 2
#Printing the last item of the list
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

#example 3
#Return the third, fourth, and fifth item:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#example 4
#returning the items from the beginning until "kiwi":
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

#example 5
#Returning from "cherry" to end
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#example 6
#returning the items from "orange" (-4) to, but NOT including "mango" (-1):
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#example 7
#Check if "apple" is present in the list:
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

#Change List Items
#example 1
#Changing the second item:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#example 2
#Changing the values  "banana" and "cherry" with the values "blackcurrant" and "watermelon":
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#example 3
#Changing the second value by replacing it with two new values:
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

#example 4
#Changing the second and third value by replacing it with one value:
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

#example 5
#Insert() statement:
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#Add List Items
#example 1
#append() statement
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#example 2
#Insert() statement at a position
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#example 3
#Extend() statement:
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#example 4
#Add elements of a tuple to a list w extend()
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)


#Remove List Items
#example 1
#Remove "banana"
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#example 2
#Remove the first occurance of "banana"
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

#example 3
#The pop() method removes the specified index
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#example 4
#Remove the last item
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#example 5
#Remove the first item w "del"
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#example 6
#Delete the entire list w "del"
thislist = ["apple", "banana", "cherry"]
del thislist

#example 7
#Clear the list content w "clear()"
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#Loop Lists
#example 1
#Printing all items in the list, one by one
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#example 2
#Print all items by referring to their index number
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

#example 3
#Print all items, using a while loop to go through all the index numbers
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#example 4
#A short hand for loop that will print all items in a list
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

#List Comprehension
#example 1
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

#example 2
#Only accept items that are not "apple"
newlist = [x for x in fruits if x != "apple"]

#example 3
#With no if statement:
newlist = [x for x in fruits]

#example 4
#You can use the range() function to create an iterable
newlist = [x for x in range(10)]

#examplr 5
#Accept only numbers lower than 5
newlist = [x for x in range(10) if x < 5]

#example 6
#Set the values in the new list to upper case
newlist = [x.upper() for x in fruits]

#example 7
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = ['hello' for x in fruits]
print(newlist)
#example 8
#Return "orange" instead of "banana"
newlist = [x if x != "banana" else "orange" for x in fruits]

#Sort Lists
#example 1
#Sort the list alphabetically
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#example 2
#Sort the list numerically
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

#example 3
#Sort the list descending
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

#example 4
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

# example 5
#Sort the list based on how close the number is to 50:
def myfunc(n):
  return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

#example 6
#sort() would output upper first, so
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

#example 7
#Reverse the order of the list
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

#Copy Lists
#example 1
#Make a copy of a list with the copy() method
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#example 2
#Make a copy of a list with the list() method:
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

#Join Lists
#example 1
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

#example 2
#Appending list2 into list1:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)
print(list1)

#example 3
#Using the extend() method to add list2 at the end of list1:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)



