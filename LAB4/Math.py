#exercise 1
import math

def radian(n):
    m = (n * math.pi) / 180
    yield round(m, 6)

n = int(input())
for num in radian(n):
    print(num)

#exercise 2
import math

def trapezoid_area(height, base1, base2):
    med_line = (base1 + base2) / 2
    area = med_line * height
    yield area

height = float(input())
base1 = float(input())
base2 = float(input())
for area_trapezoidal in trapezoid_area(height, base1, base2):
    print(area_trapezoidal)

#exercise 3
num_sides = int(input("number of sides: "))
lenght_side = int(input("thelength of a side: "))
area = num_sides * pow(lenght_side,2) * (1/4)
print("The area of polygon is: " + str(area))

#exercise 4
import math

def paralelogram_area(height, base):
    area = height * base
    yield area

height = float(input())
base = float(input())

for area_of_p in paralelogram_area(height, base):
    print(area_of_p)