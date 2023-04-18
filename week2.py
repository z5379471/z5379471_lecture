# WEEK 2
# objects
# 1. primitive objects
# --> textual data
#      e.g. tic = " QAN.AX" --> quotes(''/""/'''/""") are important
#      tic = QAN.AX
#      print(tic) ---> (have : NameError: name 'QAN' is not defined)
#      str1= ' a single line' / "a single line"
#      str2= '''mutiple lines'''/ """ mutiple lines"""
#      e.g. str1 = 'THis string cannot span
#      more than one line'--->  ( have the : SyntaxError: unterminated string literal (detected at line 10))
#      e.g. str1= 'John said, "Let's learn Python together".'
#      print (str1) --> have : SyntaxError: unterminated string literal (detected at line 12)
#      --> by using triple quotes:
#      str1= '''John said, "Let's learn Python together".'''
#      str2=  """John said, "Let's learn Python together"."""
#      --> by using backslash(\) to escape the quotation marks
#      str3= "John said, \"Let's learn Python together\"."
#      str4='John said, "Let\'s learn Python together".'
#--> interger and floating point numbers ( numerical data)
#      interger : the number without point (1 , -1) ;
#      floating point number : the number with point (1.0 , 4/2,1/3)
#      test value:
i =1
test = i == 1 # --> True (== : to test if i is equal to 1)
print(test)
# Be careful when comparing floating point numbers !!!
x= 0.2+0.2+0.2
print(x) # --> x= 0.6000000000000001
print(x==0.6) #--> False

x= 0.2+0.2
print(x) # --> x= 0.4
print(x==0.4) #--> Ture

import math # --> math is library, isclose is the function from math, isclose checks two vlaues close each other
f = 0.2 + 0.2 + 0.2 # --> True
print(math.isclose(f, 0.6) )

#--> booleans (bool): A type for True/False data --for logic testing
#    comparing objects :
#    inequality tests:
print( 1 < 2 ) # `True`
print( 1 > 2 ) # `False`
print( 2 >= 2 ) # `True
#    equality tests:
1 == 2 # --> `False`
2 == 2 # --> `True`
#    The following raises an error
#    1 = 1 # This is an assignment statement, not a comparison! /
#    logic operation on bool
#    not Ture #--> `True`
#    True and False # --> `False`
#    True or False #--> `True`
#---> Nonetype : None
#     None does not mean 0 , False , or an empty string.
#     None represents a null value, that's it.
# 2+None # --> TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'
#     check the type of an object
i =1
print(type(i))

xstr = '1'
print(type(xstr)) #--> <class 'str'>

test = x == xstr
print(test)
print(type(test)) # --> <class 'bool'> ( the true or false data)

print(3+2) #--> 5
print('3'+'2') #--> 32

a= '3'+'2'
#b= 3+a #--> TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(type(a)) # --> <class 'str'> !!!!
#print(b)

#print('3'+3) #--> TypeError: can only concatenate str (not "int") to str
print('3'*3) #--> 333

# Interacting with objects using methods and attributes
# e.g. yfinance.download(tic, start, end, ignore_tz=True)
# attribute : "dot"
# method : 'download' is a method/function belong to yfinance

# Namespaces :
# built-in namespaces > global namespaces > local namespaces
# built-in namespaces : built-in functions

x= 'abc'
x=str('abc')
# upper(x) #--> Error: upper is not a built-in function // NameError: name 'upper' is not defined. Did you mean: 'super'?
xup= str.upper(x) #--> upper is a fuction which belongs to str class
print(xup)

y= 'abc'.upper() # the another method to use the upper fuction
print(y)

# the other methods in the str class
# e.g. str.lower()
weird_case = "My fUnNy tYpEcAsE sTrInG"
weird_case_lower = weird_case.lower() # --> "my funny typecase string"
print(weird_case_lower)
weird_case_upper = weird_case.upper()
print(weird_case_upper)
weird_case_lower= weird_case.upper().lower()
print(weird_case_lower)

# method calls with parameters
# e.g. str.center(width[,fillchar])
# Center the word "Hi" in a line of 40 characters (width)
print("Hi".center(40)) #-->                    Hi
print("Hi".center(40,"0")) #--> 0000000000000000000Hi0000000000000000000

# formating strings
# e.g. a = True
#      b = 5
#      print("The value of a is a and the value of b is b")
# Output:
# "The value of a is a and the value of b is b"
# using f-string
a = True
b = 5
print(f"The value of a is {a} and the value of b is {b}") #--> The value of a is True and the value of b is 5
# format function
print("The value of a is {} and the value of b is {}". format(a,b)) #--> The value of a is True and the value of b is 5

# Variable names : rules and conventions
# recap: Python naming rules ).
# Names must start with a letter or underscore ("_").
# Names can only contain alphanumeric characters and underscores.
# Names are case-sensitive. (a, A,aa,AA,Aa)
# All these rules apply to any variable, function, or class we create.
# reserved words
#e.g. Using a reserved keyword as a variable name produces an error!
# import = 'some string' # --> import is a reserved word and this will raise the following exception:
# SyntaxError: invalid syntax
#You should avoid certain variable names, even though they do not violate the Python syntax.
# Example: Built-in function names You can create variables with the same name as some of Python built-in functions.
#E.g. sum() is a built-in function, but sum is not a reserved keyword
x= str(5)
print(x) #--> '5'
print(type(x)) #--> <class 'str'>

str = "very bad idea!"
x= str(5)
print(x) #--> TypeError: 'str' object is not callable

str2= "very bad idea!"
x= str(5)
print(x) #--> '5'

str =5
x= str(8)
print(x) #--> TypeError: 'int' object is not callable
# naming variables in PEP 8 - Style Guide for Python Code
# stanard variables : by using lower-case letters with underscores
# constant variables : by using upper-case letters with underscores
# class : by using a capital letter followed by lower-case letters : Variable


# Adding functionality: Modules and packages
# e.g. yfinance: a package
# one module can be a package as well

# in-class exercise 2
length = 56
width = 33
height = 30.5
volume = length * width * height
print(volume) #--> 56364.0 (cm^3)
print(f'the volume of a box is {volume} cubic centimeters.')
# --> the volume of a box is 56364.0 cubic centimeters.
print ('the volume of a box is {} cubic centimeters'. format(volume))
# --> the volume of a box is 56364.0 cubic centimeters.

# Python data structures
# Used to store and organize data.
# Used to arrange data on a computer so that it can be accessed and updated efficiently.
# four common data strutures:
# 1. List
# list class, a collection of objects
# list class is mutable ( can be added and moved out)
# e.g. mix the list
lst = [1, "string", True, None]
print(lst) #--> [1, 'string', True, None]
print(type(lst)) #--> <class 'list'>

# list--> empty lists
lst= []
lst= list()
print(lst) #--> []

lst=[]
lst2= [None]
print(lst== lst2) #--> False
test= lst ==lst2
print(test) #--> False

# list--> indexing
# zero-based indexing
lst = [1, "string", True, None]
print(lst[1]) #--> 'string'

# negative indexing (the last element is -1)
lst = [1, "string", True, None]
print(lst[-2]) #--> 'True'

# some errors raised in indexing code
lst = [1, "string", True, None]
print(lst[-5]) #--> IndexError: list index out of range

# list--> slicing
# lst[start: end] --> the start one is included but the end one is out of the list range
lst = ["a", "b", "c", "d", "e", "f"]
print (lst[1:4]) #--> ['b', 'c', 'd'] --> only includ 1,2,3 indexing (3 elements)
print (lst[-4:-1]) # --> ['c', 'd', 'e']
print (lst[0:4]) # --> print (lst[:4])
print (lst[1:6]) #--> print(lst[1:])
print(lst[:]) #--> ['a', 'b', 'c', 'd', 'e', 'f'] the whole list

lst = ["a", "b", "c", "d", "e", "f"]
print(f"lst[:3] gives {lst[:3]}")
print(f"lst[0:1000] gives {lst[0:1000]}") # --> lst[0:1000] gives ['a', 'b', 'c', 'd', 'e', 'f']
print (lst[1:10]) #--> ['b','c', 'd', 'e', 'f']

# list--> append method
# to append an element to the end of a list
lst_a =[1]
# using list class attribute(.) to access the append method
list.append(lst_a,2)
print(lst_a) #--> [1, 2]
# using list instance attribute(.) to access append method
lst_a=[1]
lst_a.append(2)
print(lst_a) #--> [1, 2]
# The append method will modify the list in place. It does not return a new list!

# list--> extend method
lst_a = [1]
lst_b = [2, 3]
lst_a.extend(lst_b)
print(lst_a) # --> lst_a now is [1, 2, 3]

# list --> removing method
# remove(x) --> remove x out of the list
# pop()--> remove the last object in the list
# pop(x) --> remove x
# clear() --> remove all elements in the list
# Example :
# remove()
lst = [1, "string", True, None]
lst.remove(True)
print(lst) #--> ['string', True, None] !!!
lst = [0, "string", False, None]
lst.remove(False)
print(lst) #--> ['string', False, None] !!!
# --> becasue :
print(1==True) #--> True
print(0== False) #--> True
# pop()
lst = [1, "string", True, None]
lst.pop(True)
print(lst) #--> [1, True, None] ????
# clear()
lst = [1, "string", True, None]
lst.clear()
print(lst) #--> []

# list--> reserve method
# Used to reverse the order of items in a list in place.
lst = [1, 2, 3]
lst.reverse()
print(lst) #--> [3, 2, 1]

# list--> built-in len function
# how many items in the list
lst = [1, "string", None, True]
no_of_items =len(lst)
print(f"lst has {no_of_items} items") #--> lst has 4 items

# list--> split method
# string. split(separator, maxsplit)
line = "welcome to the class"
x = line.split()
print(x) #-->['welcome', 'to', 'the', 'class']
# e.g. in-class exercise 3 !!!
#'From firstname.surname@unsw.edu.au Tue Oct 06 10:10:15 2020'
# Challenge: Can you get the domain name in one line?
str= "From firstname.surname@unsw.edu.au Tue Oct 06 10:10:15 2020" #--> this list has 7 items
domain= str.split()[1].split('@')[1]
# str.split()[1] --> split 1 indexing string('firstname.surname@unsw.edu.au') out of the str
# split('@')[1] --> use @ seperate 'firstname.surname@unsw.edu.au' into 2 items and split the 1 indexing string out of the whole
print(domain) #--> unsw.edu.au

# 2. Tuples
# tuple is similar to list but tuple is immutale (can not be changed)
# and tuple is expressed by () not [].
# e.g. tup = ('word', 5, False)
# tuples--> indexing and slicing --> identical to the list
# tuples--> packing and unpacking
# e.g. unpacking
tup= (1,2)
(a,b) =tup
print(f"'a' is {a} and 'b' is {b}")
print("'a' is {} and 'b' is {}".format(a,b)) #--> 'a' is 1 and 'b' is 2
# Python does not care whether you use parentheses when packing (creating)
# or unpacking tuples.
# e.g. have the same correct output
a,b = 1,2
(a,b)=(1,2)
(a,b) =1,2
a,b=(1,2)

# 3. sets
# the set is the collection of objects which appear only once
# by using {}
set={1,2,3,3,3}
print(set) #--> {1,2,3}
# Unlike Lists and Tuples, you cannot create an empty set using curly braces {} .
# if you want to create an empty set, you must use set method, set()
empty_set =set()
# sets--> add method
s = set()
s.add("QAN.AX")
print(s)

Common set methods: add & remove

s = set()
s.add("QAN.AX")
s.add("WES.AX")
s.add("CBA.AX")
s.add("CBA.AX")

# s is {"QAN.AX"} # s is {"QAN.AX", "WES.AX"} # s is {"QAN.AX", "WES.AX", "CBA.AX"} # s is {"QAN.AX", "WES.AX", "CBA.AX"} (so no change)

print(f"After adding objects, s is {s}")

# to check if an object in inside a set
s={1,2,3}
print(1 in s) #--> True
print(1 not in s) #--> False
# to check the number of elements in a set
s={1,2,3}
n_of_elements= len(s)
print(f"s contains {n_of_elements} in the set") #-->s contains 3 in the set

# sets--> differences from the lists and tuples
# sets (unordered)do not have indexing and slicing because sets are not intrinsically ordered.

# 4. Dictionaries
# Python and dictionaries {}
# --> each key appaers exactly once and different key can have the same value.
# dictionaries --> create dictionaries
prc_dic = { '2020-01-02': 7.1600,  #--> { key : value }
            '2020-01-03': 7.1900,
            '2020-01-06': 7.0000,
            '2020-01-07': 7.1000,
            '2020-01-08': 6.8600,
            '2020-01-09': 6.9500,
            '2020-01-10': 7.0000, }
print(prc_dic)
# ask for the value []
print(prc_dic['2020-01-02']) #--> 7.16
# to add a key-value pair to a dictionary
# e.g.
prc_dic = {'2020-01-02': 7.1600,
           '2020-01-03': 7.1900,
           '2020-01-06': 7.0000, }
prc_dic['2020-01-02']= 7.2000 #--> to overwrite the previous value
prc_dic['2020-01-07']= 7.5000 #--> to create a new pair
print(prc_dic) #--> {'2020-01-02': 7.2,
#                    '2020-01-03': 7.19,
#                    '2020-01-06': 7.0,
#                    '2020-01-07': 7.5}
# to remove a pair
# --> by using the pop() method
d = {'a': 1, 'b': 2 }
d.pop('a')
print(f"After popping 'a', d is now {d}")
# the dictionaries' key must be immuatable ( except list[], set{},dic{})
# the dictionary is ordered?
