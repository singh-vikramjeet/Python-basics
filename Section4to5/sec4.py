# // *************** Section 4: Functions and Modules in Python **********

# // ************* Passing Arguments to Functions in Python ******************

def add(a,b):
    print(a+b)
   

add(10,20)

# // *************** Making Function Return Value in Python ********************

def add(a,b):
    c = a + b
    return c

result = add(10,70)
print(result)

# // *************** Passing Functions as Arguments in Python *******************

def add(a,b):
    return a + b

def square(c):
    return c * c

result = square(add(2,3))
print(result)

# // *************** Modules in Python *************************************

import random

for x in range(5):
    result = random.randint(1,6)
    print(result)


# // ***************** Exception Handling and File Handling in Python ***************

# // ******************* Errors and Exceptions in Python ******************

def function1(a,b):
    print(a/b)

function1(20,0)
# funtion1 will throw divide by zero exception
print("Hello")

# // ******************** Exception Handling in Python **********************

try:
    a = 20
    b = 0
    print(a/b)
except ZeroDivisionError:
    print("There is a divide by zero error!")

# // ******************* Finally Block ***************************

try:
    a = 20
    b = 5
    print(a/b)
except ZeroDivisionError:
    print("There is a divide by zero error!")
finally:
    print("This going to execute no matter what")

# // ***************** File Handling ****************************
# open the file for writing
file = open("demo.txt",'w')
file.close()


# // **************** Reading Data from a file *******************

file = open("demo.txt",'r')
content = file.read()
# You can specify how many bytes to read from the file using the first parameter in the read function
# content = file.read(10)

# readline function reads single line
# content = file.readline()

print(content)
file.close()

# // ****************** Adding Data to the file ***********************

file = open("demo.txt","w")
file.write("This is the text written to the file")
file.close()

file = open("demo.txt",'r')
result = file.read()
print(result)

# // ****************** Appending to a file ****************************

file = open("demo.txt",'w')
file.write("This is the text written to the file")
file.close()

file = open("demo.txt",'r')
content = file.read()
print(content)
file.close()

# Open the file again in append mode
file = open("demo.txt",'a')
file.write("\nThis is the new appended line")
file.close()