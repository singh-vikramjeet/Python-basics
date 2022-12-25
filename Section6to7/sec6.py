# //********************* Data Structures in Python ***************

# // *************** Dictionaries ********************************

# Dictionaries store key-value pairs just like Hash table in other languages

people = {
    "John":32,
    "Rob":23
}
print(people["Rob"])

# // **************** Dictionary Functions ***********************

numbers = {
    1: "one",
    2 : "two",
    3: "three"
}

# This checks if a key is present in the dictionary or not
# Returns either true or false
print(2 in numbers)

# get function
# Key "2" is present in dicitionary
print(numbers.get(2))

# For key that is not present in the dictionary,
# the default messages is None, but we can modify it
# using the second argument in get function
print(numbers.get(5, "Key not found"))


# // ***************** Tuples *****************************

# A tuple is similar to list, the only difference is that the
# values in tuple are immutable and cannot be changed

fruits = ("Apple","Mango","Peach")
# You cannot reassign the values in tuple
# fruits[0] = "Blueberry"
# The line above will not work
print(fruits[1])

# // ******************* List Slicing ******************

numbers = [0, 100, 200, 300, 400, 500, 600]

# prints elements at index 2, 3 and 4
print(numbers[2:5])

# prints elements before index 3 (LHS of index 3)
print(numbers[:3])

# prints elements after index 3 (RHS of index 3)
print(numbers[3:])

# specify an interval between each element
print(numbers[1:6:2])

# // ******************** List Comprehension ***************

# Rule to print a square of numbers from 0 to 4
# range(5) denotes numbers from 0 to 4
list = [x**2 for x in range(5)]
print(list)

# Creates a list which includes only even elements
evenList = [x**2 for x in range(10) if x**2 % 2 == 0]
print(evenList)

# // ****************** String formatting *******************

numbers = [2022,12,25]
newString = "Numbers:{0}/{1}/{2}".format(numbers[0],numbers[1],numbers[2])
print(newString)
 
a = "{x}/{y}".format(x=100,y=200)
print(a)

# // ****************** String functions *********************

# String function to join list elements by a comma or something else
print(",".join(["Apple","Blueberry","Strawberry"]))

# string function to replace a substring with new string
print("Hello There".replace("There","World"))

# To check if a string starts with given substring
newString = "This is a string"
print(newString.startswith("This"))
print(newString.endswith("string"))

# To convert the string to uppercase
print(newString.upper())

# // ****************** Numeric functions *********************

# Use min or max function to get the respective values from a list
print(min(1,2,3,4,5))
print(max(1,2,3,4,5))

# function to print absolute value of any number
print(abs(-203))
