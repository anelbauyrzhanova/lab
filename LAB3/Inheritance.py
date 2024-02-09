#Examples
#Example 1
#Create a class named Person, with firstname and lastname properties, and a printname method:
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)
#Use the Person class to create an object, and then execute the printname method:
x = Person("John", "Doe")
x.printname()

#example 2
#Create a class named Student, which will inherit the properties and methods from the Person class:
class Student(Person):
  pass

#example 3
#Use the Student class to create an object, and then execute the printname method:
x = Student("Mike", "Olsen")
x.printname()

#example 4
#Add the __init__() function to the Student class
class Student(Person):
  def __init__(self, fname, lname):
    #add properties etc.

#example 5
#To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lastname = lname
    
    def printname(self):
        print(self.firstname, self.lastname)
class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)
x = Student("Mike", "Olsen")
x.printname()

#example 6
# super() function that will make the child class inherit all the methods and properties from its parent:
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

x = Student("Mike", "Olsen")
x.printname()

#example 7
#Add a property called graduationyear to the Student class
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019
#examplr 8
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)

#example 9
#Add a method called welcome to the Student class
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

#Exercises
#exercise 1
class Student(Person):
#exercise 2
class Person:
  def __init__(self, fname):
    self.firstname = fname

  def printname(self):
    print(self.firstname)

class Student(Person):
  pass

x = Student("Mike")
x.printname()
