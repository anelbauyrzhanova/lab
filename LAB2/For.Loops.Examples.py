#Examples

#example 1
#printing each fruit in a fruit list:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#example 2
#Looping through the letters in the word "banana":
for x in "banana":
  print(x)

#example 3
#with "break" statement we can stop the loop before it has looped through all the items
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
  
#example 4
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

#example 5
#with "caontinue" statement we can stop the current iteration of the loop, and continue with the next
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#example 6
#The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
for x in range(6):
  print(x)

#example 7
#using the start parameter (not 0):
for x in range(2, 6):
  print(x)

#example 8
#Increment the sequence with 3 (default is 1)
for x in range(2, 30, 3):
  print(x)

#example 9
#The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
for x in range(6):
  print(x)
else:
  print("Finally finished!")

#exanple 10
#The else block will NOT be executed if the loop is stopped by a break statement.
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!") 

#Nested Loops

#example 1
#Printing each adjective for every fruit:
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)

#example 2
#Using "pass" statement for using "for" w no content
for x in [0, 1, 2]:
  pass

  
  

  