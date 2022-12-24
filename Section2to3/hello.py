
# // Hello world in python
msg = "Hello World!"
print(msg)

# //Division in python
# //This division gives 5.0 as result (with Decimal point)
print(500/100)

# //To get the answer without decimal point, do this instead
print(500//100)

# // How to do exponentiation in Python
result = 2**3
print(result)

# // How to take Square root?
result1 = 49**(1/2)
print(result1)

# Modulo operator in Python is same as other languages

# //Strings in python
# //with single quotes
str1 = 'This is a string with single quotes'
# //with double quotes
str2 = "This is a string with double quotes"

print(str1)
print(str2)

#//Accept user input in python
input('Please enter a value')

# //String concatenation in Python
str = "hello" + "world"
print(str)

# // Multiplying a string by a number
str = "bob"*3
print(str)
# output is bobbobbob

# //To delete a value stored in a variable, use del function
a = "variable"
print(a)
del a
print(a)

# In place operator in Python

age = 39
age += 1
print(age)

# ****************** Section 3: Control Structures *********************

# //****************if statement in python************

# age = int(input("Enter your age"))

#//input function takes input in the form of string
# // To convert string value to int, we used the int function above

if age >= 18:
    print("You are an adult")
else:
    print("You are not an adult")

# // ************* elif (else if) statement in python**********

marks = int(input("Enter your marks"))

if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks < 60:
    print("Grade D")

# // ***************** Lists in Python *****************

#// A list to store string values
names = ["Mike", "John", "Rob"]
print(names)
print(names[2])

#// A list to store number values

numbers = [1, 2, 3, 4, 5]
print(numbers[4])

#//Create an empty list
abc = []
print(abc)

# // ********************* List Operations in Python ***************

numbers = [1, 1, 1, 1, 1]

#//To insert a value at a particular index in the list
#//Line below inserts a value of 5 at index 2 and deletes the previously stored value
numbers[2] = 5
# // output is [1, 1, 5, 1, 1]
print(numbers)

newNumbers = [2, 2, 2, 2, 2]

# // To concatenate two lists in Python
print(numbers+newNumbers)

# // To replicate and concatenate the same list
print(numbers * 3)

fruits = ["Apple", "Mango", "Peach"]

# To check if an element is present in the list
print("Apple" in fruits)
# Above line will print true
print("Orange" in fruits)
# Above line will print false


# // ********************* List Functions in Python *******************

fruits = ["Apple", "Mango", "Peach", "Orange"]

#// Append operation for list
fruits.append("Banana")
fruits.append("Blueberry")
print(fruits)

# // To calculate the length of the list
print(len(fruits))

# // To insert an item at a particular position
fruits.insert(1, "Banana")
print(fruits)

# // To get an index of particular item in the list

print(fruits.index("Peach"))


# // ********************* Range Function in Python *********************

#// Use the range function to make a list of numbers from 0 to 9
numbers = list(range(10))

# 3 is the starting number (inclusive)
#8 is the ending number (exclusive)
output = [3,4,5,6,7]
numbers = list(range(3,8))

# We can also specify the interval between two elements in the
# list using the third argument in the range function

numbers = list(range(1,30,5))

print(numbers)

# // *************** Code Reuse and Functions in Python ****************

#// Creating a function
def function1():
    print("name")
    print("apple")
    print("new york")

# // Calling a function 2 times
function1()
function1()


# // *************** For Loop in Python ****************************

for x in range(1,11):
    print(x)

fruits = ["Apple", "Banana", "Peach", "Orange"]

for x in fruits:
    print(x)

# // for loop to print even numbers from 0 to 20
for x in range(0,21,2):
    print(x)
# // **************** Boolean Logic in Python ************************

username = "admin"
password = "admin123"

if username == "admin" and password == "admin123":
    print("Valid User")
else:
    print("Invalid User")

# Boolean operator in python
# && in Java is equivalent to: and
# || in Java is equivalent to: or

# // **************** While Loop in Python **************************

counter = 0
while(counter <= 10):
    print(counter)
    counter+=1