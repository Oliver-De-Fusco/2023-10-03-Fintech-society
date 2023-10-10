## anything after a # are comments and will not be interpreted as code
## toggle the # by moving your cursor and pressing CTRL + / in vscode or removing "# "
## lines starting with ## is not valid code, even when un-commented completely
## make sure to save the file when you un-comment to run the code

print("Hello world") # print is a function that will display its input to the terminal, its input is contained by : ()

## Data types

# a = 10 # is a interger

## you can use _ as a placeholder, so x = 10_000 is the same x = 10000

# b = 1.0 # is a float, the presence of the decimal point makes it a floating interger

## both intergers and floats can be used with the basic math operators such as +, -, / (divide) and * (multiply)
## x ** y , x to the power of y
## x %  y , modulus which returns the remainder of x when divided by y, remainders of zero means it is a multiple, used for fizzbuzz and hashmaps
## x // y , is x / y rounded down and returns an interger instead of a float

# c = True # This is a boolean, only two values are possible (True and False), also used in if statements.
# d = "string" # strings are surrouned by " or ' , they contain letters. strings can be added to the end of each other by using +
## you can also "format" strings with "{}, {}".format(value1, value2) or f"{value1}, {value2}"

## Because python is dynamically typed it means that you can overwrite a previous variable type with a different type

# print("1" + "1") # The output is 11 as "1" is not an interger, it is a string, math is not performed and instead it is concatenated

## we can assign two variables at once on the same line by using a ,
# a, b = 10, 1.0
## this is not reccomended, with many variables this can quickly become unclear what is assigned to what but it does come in use with loops

## You can convert other variables to other types using a function
# print(int("1") + int("1")) # Strings are converted to ints and then added
# print(str(1) + str(1)) # ints are converted to strings and concatenated
## float() converts numbers and strings to floats, however by inputting "inf" you can get a value of infinite, good for when you need an initial comparison, negative infinity is just -float("inf") 
## there are also similar functions for data structures

## Data structures

## lists can store multiple types of data and at any lengths

example_list = ["a","b","c","d","e","f"]
# example_list2 = ["b",1,"t","f",6.9,"k",True]

# tuples = (1,2,3) # tuples are similar to lists but cant be modified
# print(example_list[1]) # you can access elements by using the index, all indexes are zero indexed - they start at zero, using negative indexes will start at the end and move forwards
# print(example_list[2:5]) # slices can be used to get a range of data, in the form [start:end], end is exclusive so if you want to start at "c" and want to include "e", end should be equal to 5, see below diagram
## you can leave the numbers from the slice blank and get the numbers to either the start or end depending on the side you leave it blank
# print(example_list[2:])

## The index will get the number to the left, negative numbers work backwards starting at -1 but also get the left number 
##  +---+---+---+---+---+---+
##  | a | b | c | d | e | f |
##  +---+---+---+---+---+---+
##  0   1   2   3   4   5
## -6  -5  -4  -3  -2  -1

## dictionaries store data to a key, you can access data by giving it a non-mutable key

# dictionary = {"first" : 10, "apple" : "grapes", tuples : "this is a tuple as a key"}
# print(dictionary["apple"])


## Loops

# example_list = ["a","b","c","d","e","f"]
# example_list2 = ["b",1,"t","f",6.9,"k",True]

## For Loops
## Loops iterate through a given list, they assign the value to a variable, in this case it is called x, and then run the code indented below
## Code intendation is forced in python, for python to know what to run next you use tab, vscode will do indentation for you
## when it is done running the code below where it is declared, it will assign the variable to the next value in the list

# for x in example_list: # this list prints out the data one by one from the list example_list
#     print(x)

## when a for loop has exhasted all its values it will exit and python will run the next code below the indented code
## using the function, range(end), it will generate a list from 0 to end (exclusive) to loop through

# for interger in range(100): # print intergers 0 to 99
    # print(interger)

## range can take a start value and step : range(start, end, step)

# for interger in range(2,20,2): # print out only the even numbers starting at 2, ending at 18
    # print(interger)

## another fuction, enumerate, will give a tuple in the form (current_index, value_at_index)
## we can assign more than one value at once by using a comma much like assigning a variable in on one line

# for index, value in enumerate(example_list):
    # print(index, value)

## while loops
## while loops operate while the condition is True (see logic flow)

# x = 0
# while x < 10:
#   print(x)
#   x += 1

## all loops can be broken early by using the key word : break, or when in a function : return

## logic flow and if statements

## code does not run unless the condition is True

# x = 10
# if x == 10:
#   print("x is equal to 10")
# elif x == 9: # if the first condition fails it tries this condition, you can add many more of these
#   print("x is equal to 9")
# else: # if none of the conditions match then below will run, line 104 will not run if a condition is met, without "else:" (and indentation) line 104 will always run.
#   print("x is not equal to 10 or 9")

## see https://docs.python.org/3/library/stdtypes.html#comparisons or below for list of ways to compare
## ==, equal too , True only when the values are equivalent
## is, is identical, True only when they are exactly the same, it is a check for the same identity, (used for object oritenated programming)   
## < or >, greater than or less than, this checks if a value is greater than or less than another and will return True based on the evaluation
## <= or >=, greater than or less than or equal too, same as above execpt it is also True when they are both the same
## !=, not equal to, is True for all conditions execpt for when it is equal too
## not x, inverts the condition, if "True:" then "if not True:" is False and will not enter the condition
## x or y, if either condition x or y is True then return True

## you can also use comparisons to assign or return boolean values

# x = 10 == 10 # True

## you can use the keyword "in" to check if a value is in a list.

# x = 3
# if x in [1,2,3,4,5]:
    # print(f"{x} is in the list")

## functions
## functions take their name from mathematics where they take an input and give an output based on their input, however, unlike math we can use logic to control the output
## functions are defined using "def [function name]():" then the code below is the code that is ran when [function name] is called using ()

# def function1():
    # print("This is a function")
# 
# function1()
# function1()

## functions should always use the key word, return, this is how a function outputs its value. A function should not have any side effects or un-intentional behaviour such as modifing the inputs 

# def function1():
    # return "This is a function"
# 
# print(function1())

## functions take inputs by defining required variables in () and refrencing them within the code below, the function adds both its inputs

# def function1(input1,input2):
    # return input1 + input2
# 
# print(function1(1,2)) # 3

## The inputs can also be made optional by assigning a value when declared in (), you can also assign it to a previously declared variable

# def function1(input1=1, input2=2):
    # return input1 + input2
# 
# print(function1()) # 3
# print(function1(3,4)) # 7
# print(function1(input2=5)) # 6

## As a general tip, a single function should not need to be longer than 30 lines or more than 3 levels of indentation as it begins to become un-readable.
## To avoid this,put some of the code into another function that has a smaller responsibilty, this makes it easier to debug and test.
## You can also reduce indentation by discarding unwanted variables at the top of the function instead of within the code or inverting conditions

## Recursion and sub-functions

## functions can also call other functions or even themselves and can act similar to a loop, the below code finds the fibonacci number at a index (0-indexed) using recursion

# def fibonacci(n):
    # if n <= 1: # This is the base case, a recurisve function without a base case will continue forever
        # return n 
# 
    # return fibonacci(n-1) + fibonacci(n-2) # fibonacci is defined as the previous two numbers added together
# 
# print(fibonacci(20))

## recursive functions get out of hand quick so ensure the base case (the condition to stop) is solid, e.g. instead of using == , in the base case, use <=.
## for this algorithm, to find larger numbers more quickly (or at all) you will need to store previously calculated values for the inputs using a cache
## another function can also be defined within a function
## functions or variables declared inside loops or functions cannot be refrenced above (in terms of indentation) the same loop or function, this is reffered to as scope

## By using *args when defining the inputs in () you can take any number of arguments, args will be treated as a tuple.
## **kwargs will take key word arguements, kwargs is treated like a dictionary. args and kwargs would be the variable names

## There are still a lot more layers to python such as classes, generators, file IO, decorators and everything else both the default and third party libaries can offer.
## It also good to have a basic understanding of computer science and algorithms which leetcode.com can help with