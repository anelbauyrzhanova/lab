#Examples
#example 1
#Add 10 to argument a, and return the result:
x = lambda a : a + 10
print(x(5))

#example 2
x = lambda a, b : a * b
print(x(5, 6))

#example 3
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

#example 4
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
print(mydoubler(11))

#example 5
def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)
print(mytripler(11))

#Exercises
#ex 1
#creating a lambda function that takes one parameter and returns it
x = lambda a : a
