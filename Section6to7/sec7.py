# // *************** Functional Programming in Python ************

# Functional programming basically means one function can be passed as an argument
# to another function

def add_ten(x):
    return x+10

def twice(func, arg):
    return func(func(arg))

print(twice(add_ten,10))

# // *************** Lambdas in Python *****************

result = (lambda x: x**2)(30)
print(result)

# // **************** Map in Python *******************

def add(x):
    return x+2

newlist = [10,20,30,40,50]

# map function allows us to perform a function on every element of a list
result = list(map(add,newlist))
print(result)

# You can also use a lambda instead of creating an add function
result = list(map(lambda x:x+2,newlist))
print(result)


# // ******************** Filters in Python ***************

# filter function allows us to filter out the elements in a list using a lambda function

newlist = [1,3,4,5,7,2,9,11,13]

result = list(filter(lambda x: x % 2 == 0,newlist))
# this filters out the odd numbers in the list
print(result)

# // ********************* Generators in Python ******************

def function():
    counter = 0
    while counter < 5:
        yield counter
        counter += 1

for x in function():
    print(x)

# A generator to create a list of even numbers

def even_numbers(x):

    for i in range(x):
        if i % 2 == 0:
            yield i

print(list(even_numbers(20)))