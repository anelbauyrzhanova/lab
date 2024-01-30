#Examples

#example 1
#With "while" loop we can execute a set of statements as long as a condition is true
i = 1
while i < 6:
  print(i)
  i += 1

#example 2
#with the "break" statement we can stop the loop even if the while condition is true
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

#example 3
#with "continue" statement we can stop the current iteration, ,and continue with the next
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

#example  4
#with "else" statement we can run a block of code once when the condition no longer is true
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
 
  