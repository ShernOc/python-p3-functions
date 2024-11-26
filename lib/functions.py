#!/usr/bin/env python3
def my_function(param):
    print("Running my_function")
    return param + 1

my_function(50) # returns 51 

my_function_return_value = my_function(1)

my_function_return_value


def greet_programmer():
    print("Hello, programmer!")

greet_programmer() # Hello, programmer! 


def greet(name):
    print(f"Hello, {name}!")

greet("Maureen") # returns Hello Maureen

#|This is a default Arguments if no name is provided programmer will be provided. 
def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

greet_with_default() # return Hello, programmer
greet_with_default("Sunny") # returns Hello, Sunny 
    

def add(num1, num2):
    return num1 + num2

x = add(1,2)
print(x)
    

def halve(number):
     if (number != number):
         return None
     return number/2
num = halve(100)
print(num)


