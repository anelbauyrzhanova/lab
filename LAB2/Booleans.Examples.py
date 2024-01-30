#Examples

#example 1
#Printing messages based on whether the condition is True or False:
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#example 2
#the "bool()" function allows to evaluate any value, and give you "True" or "False" in return
print(bool("Hello"))
print(bool(15))

#example 3
#any value is evaluated as "True" if it has some sort of content except:
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

#example 4  
#an object that is made from a class with a "__len__" function that returns 0 or False:
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

#example 5
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

#example 6
#Check if an object is an integer or not:
x = 200
print(isinstance(x, int))


