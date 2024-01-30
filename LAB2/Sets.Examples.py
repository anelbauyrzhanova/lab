#Set - unordered, unchangeable, duplicates not allowed

#example 1
#True and 1 is considered the same value
thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

#example 2
#False and 0 is considered the same value
thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)

#example 3
#A set can contain different data types:
set1 = {"abc", 34, True, 40, "male"}

#example 4
#Using the set() constructor to make a set
thisset = set(("apple", "banana", "cherry"))
print(thisset)

#Access Set Items
#example 1
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#example 2
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

#Add set items
#example 1
#To add one item to a set use the add() method
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

#example 2
#To add items from another set into the current set, use the update() method
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

#example 3
#Add elements of a list to at set
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)
      
#Remove Set Items
#example 1
#Remove "banana" by using the remove() method
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

#example 2
#Remove "banana" by using the discard() method
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

#example 3
#Remove a random item by using the pop() method
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

#example 4
#The clear() method empties the set
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

#example 5
#The del keyword will delete the set completely
thisset = {"apple", "banana", "cherry"}
del thisset

#Loop Sets
#example 1
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#Join Two Sets
#example 1
#The union() method returns a new set with all items from both sets
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

#example 2
#The update() method inserts the items in set2 into set1
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

#update() and union() exclude duplicates

#example 3
#intersection_update() method keeps items that exist in both x and y
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

#example 4
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)

#example 5
#Keep the items that are not present in both sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)

#example 6
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)

#example 7
#True and 1 is considered the same value
x = {"apple", "banana", "cherry", True}
y = {"google", 1, "apple", 2}

z = x.symmetric_difference(y)

print(z)
