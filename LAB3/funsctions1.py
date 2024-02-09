#1
x = int(input())
def my_function(x):
    return x * 28.3495231
print(my_function(x))

#ex2
F = int(input())
def my_function(F):
    C = (5 / 9) * (F - 32)
    return C
print(my_function(F))

#ex3
def solve(numheads, numlegs):
    numheads = int(numheads)
    numlegs = int(numlegs)
    #4*rabbithead + 2*chickenhead == 94
    #chickenhead + rabbithead == 35
    #chickenhead = 35 - rabbithead
    
    #4*rabbithead + 2*(35 - rabbithead)==94
    #4*rabbithead +2*numheads -2*rabbithead==numlegs
    #2rabbithead +2numheads ==numlegs
    #rabbitheads = (numlegs - 2numheads)/2
    rabbithead = (numlegs - 2 * numheads) / 2
    chickenhead = numheads - rabbithead
    return chickenhead, rabbithead

numheads = input()
numlegs = input()
chicken, rabbit = solve(numheads, numlegs)
print("chickens:", int(chicken))
print("rabbits:", int(rabbit))

#ex4
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, len(numbers) - 1):
        if num % i == 0:
            return False
    return True

numbers = input().split()
for num in numbers:
    if is_prime(int(num)):
        print(num, "is a prime number")
    else:
        print(num, "is not a prime number")

#ex5

from itertools import permutations

def print_permutations(s):
    permutations_list = permutations(s)
    
    for permutation in permutations_list:
        print(''.join(permutation))


str = input()
print_permutations(str)

#ex6
def reverse_sentence(sentence):
    words = sentence.split()

    reversed_words = words[::-1]
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence

input_sentence = input()
reversed_sentence = reverse_sentence(input_sentence)
print(reversed_sentence)

#ex7
def has_33(my_list):
    if len(my_list) < 2:
        return False
    else:
        for i in range(len(my_list) - 1):
            if my_list[i] == 3 and my_list[i + 1] == 3:
                return True
        return False

nums = input().split() 
my_list = [int(x) for x in nums]  

if has_33(my_list):  
    print("True")
else:
    print("False")


#ex8
def has_33(my_list):
    if len(my_list) < 2:
        return False
    else:
        for i in range(len(my_list) - 1):
            if my_list[i] == 0 and my_list[i + 1] == 0 and my_list[i+2]==7:
                return True
        return False

nums = input().split() 
my_list = [int(x) for x in nums]  

if has_33(my_list):  
    print("True")
else:
    print("False")


#ex9
import math
def volume(radius):
    sphere_v = (4/3) * (radius**3) * math.pi
    return sphere_v

radius = float(input())
print(volume(radius))

#ex10
def unique_elements(input_list):
    unique_list = []

    for element in input_list:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list

input_str = input()
input_list = input_str.split()
input_list = [int(element) for element in input_list]
result_list = unique_elements(input_list)
print(result_list)

#ex11

def reverse_string(s):
    reversed_s = s[::-1]
    return reversed_s

str = input()
reversed_str = reverse_string(str)
def palindrome():
    for i in range(len(str)):
        if str[i]==reversed_str[i]:
            return True
        else:
            return False
        
if palindrome():
    print("It is palindrome")
else:
    print("It is not palindrome")

#ex12
def histogram(my_list):
    for i in my_list:
        print(i * "*")

nums = input().split()
my_list = [int(x) for x in nums] 
histogram(my_list)

#ex13
str_name = input("Hello! What is your name? ")
print("Well,", str_name, ", I am thinking of a number between 1 and 20.")

import random

def generate_random_number():
    random_number = random.randint(1, 20)
    return random_number

chosen_number = generate_random_number()
num_guesses = 0  

while True:
    print("Take a guess")
    num = int(input())
    num_guesses += 1

    if num < chosen_number:
        print("Your guess is to low.")
    elif num > chosen_number:
        print("Your guess is too high.")
    else:
        print("Good job, ", str_name, ". You guessed the number in ", num_guesses, " guesses")
        break

#14
import math

def volume(radius):
    sphere_v = (4/3) * (radius**3) * math.pi
    return sphere_v

def histogram(value):
    print(int(value) * "*")

radius = float(input())
volume_sphere = volume(radius)
histogram(volume_sphere)


