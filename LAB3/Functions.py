#example1
#creating a function
def my_function():
  print("Hello from a function")

#example2
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

#example3
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

#example4
#if the number of arguments is unknown, we use "*"
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

#example5
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

#example6
#if the number of keyword arguments is unknown, add "**"
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

#example7
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#example8
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

#example9
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

#example10
#if we have to use a function w no content, we use "pass"
def myfunction():
  pass

#example11
#to cpecify that a function can have only positional arguments, add ",/"
def my_function(x, /):
  print(x)

my_function(3)

#example12
def my_function(x):
  print(x)

my_function(x = 3)

#example13
#To specify that a function can have only keyword arguments, add "*,"
def my_function(*, x):
  print(x)

my_function(x = 3)

#example14
#Combine Positional-Only and Keyword-Only
def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)

#example15
#Recursion Example
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)

#Exercises
#ex 1
def my_function():
    print("Hello from a function")

#ex 2
def my_function():
  print("Hello from a function")
my_function()

#ex 3
def my_function(fname, lname):
  print(fname)

#ex4
def my_function(x):
    return x + 5

#ex5
def my_function(*kids):
    print("The youngest child is " + kids[2])

#ex6
def my_function(**kid):
    print("His last name is " + kid["lname"])