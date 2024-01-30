#If.....Else
#example 1
#If statement:
a = 33
b = 200
if b > a:
  print("b is greater than a")

#example 2
#The "elif" = "else if" as in C++
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#example 3
#The else keyword catches anything which isn't caught by the preceding condition
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#example 4
#one line if statement
a = 2
b = 330
print("A") if a > b else print("B")

#example 5
#Testing if a is greater than b, AND if c is greater than a:
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

#example 6
#Testing if a is greater than b, OR if a is greater than c:
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

#example 7
#Testing if a is NOT greater than b:
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")
#example 8
#Nested if statements:if inside of if
x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
#example 9
#using "pass" for some if statement w no content
a = 33
b = 200

if b > a:
  pass