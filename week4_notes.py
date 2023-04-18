# WEEK4
# 1. Tips: PyCharm shortcuts
# 2. more control flows
# 3. functions
# how to create a fuction :
# def function_name(< parameter expression>):
#     <function body>
# example :
def qan_tic(): #--> name of the function ; no or empty parantheses
    tic ="QAN.AX"
    print(tic) #--> assign the value of object to tic
    return(tic) #--> assign the str instance " QAN.AX" to tic
# --> but nothing will happen when run these codes
# so a function defines a set of instructions that will be executed when
# the function is called **
def qan_tic():
    tic ="QAN.AX"
    print(tic)
    return(tic)
# call the function
qan_tic() #--> QAN.AX
# example :
def qan_tic():
    tic ="QAN.AX"
    print(tic)
    return(tic)
# call the function
res = qan_tic()
print(res)
#--> QAN.AX
#    QAN.AX  --> be printed twice

# return statement
# the return statement is optional.
# if there is no return statement inside the function body, there is print None by default ???
# if print() is behind the return statement, print() will not be executed and object will exit.
# no return statement
def qan_tic():
    tic = "QAN.AX"
    print(tic)
res = qan_tic()
print(res)
# output ---> QAN.AX , None（ ⚠️）

# scope and namespaces (作用域和命名空间)
# functions are also objects, which are assigned to the variable/instance called qan_tic.
# not call the function but print the variable qan_tic
def qan_tic():
    tic = "QAN.AX"
    print(tic)
    return
print(qan_tic)
# --> <function qan_tic at 0x10f1ef4c0>
# --> means the function is store in 0x10f1ef4c0
# 0x10f1ef4c0 is the location in the computer memory and this location maybe different when you execute the code above.
# scope :
# --> local scope: the variable defined inside of the function
# belongs to the local scope, and can only used inside of the function
# --> global scope: variables created in the main program environment are called globals.
# example :
def qan_tic():
    tic = "QAN.AX" #--> tic exists in the local namespaces of qan_tic function
    print(tic)
    return
print(tic) # -->NameError: name 'tic' is not defined because tic is created inside of the function.

def qan_tic():
    tic = "QAN.AX"
    print(tic)
    return tic
tic = "WES.AX"
print(tic) #--> WES.AX (global)
qan_tic() #--> QAN.AX (local)
# LEGB rules : local , enclosed, global, built-in
def qan_tic():
    print(tic)
    return tic
tic = "WES.AX"
print(tic) #--> WES.AX (global)
qan_tic() # --> WES.AX --> because there is not local namespaces defined
# and then it will sereach for the global.

# variable shadowing
def qan_tic():
    tic = "QAN.AX"
    print(tic)
    return tic
tic = "WES.AX"
qan_tic() #--> QAN.AX

def qan_tic():
    print(tic)
    tic = "QAN.AX"
    return tic
tic = "WES.AX"
qan_tic()
# --> UnboundLocalError: cannot access local variable 'tic' where it is
# not associated with a value.

# parameters
# use comma-seperated names inside the function declaration
# use the single parameter called tic
def mk_csv_name(tic):
    tic= tic.lower()
    tic_base = tic.split('.')[0]
    return f'{tic_base}_stk_prc.csv'
name = mk_csv_name('QAN.AX')
print(name) #--> qan_stk_prc.csv
# with the optional parameter as well
def mk_csv_name(tic, show= True):
    tic= tic.lower()
    tic_base = tic.split('.')[0]
    name = f'{tic_base}_stk_prc.csv'
    if show is True:
        print(name)
    return name
name = mk_csv_name('QAN.AX') #--> qan_stk_prc.csv
# show is optional

# in-class exercise 1
test_lst= [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 22, 23, 25, 29, 30, 31]
def is_even_num(list):
    evennum=[]
    for x in list:
        if x % 2 == 0:
            evennum.append(x)
    return evennum
is_even_num(test_lst) # --> ❓❓

# comprehensions
# Comprehensions provide a concise way to construct list , dict & set containers.
# example 1 :
# list
evens=[]
for x in range(1_000_000 + 1): #--> +1 means to include the 1000000 to the range.
    if x%2==0:
        evens.append(x)
print(evens[:10]) #--> [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
# by using comprehensions
evens = [x for x in range(1_000_000+1) if x%2==0]
print(evens[:10]) #--> [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
# dictionary
# example :
pairs = [('a', 1),
         ('b', 2),
         ('c', 3), ]
# create an empty dictionary
dic= {}
# using for loop
for key,value in pairs: #--> iterate over each tuple in pairs
    dic[key]= value #--> update the dic
print(dic) #--> {'a': 1, 'b': 2, 'c': 3}
# using dic comprehension
pairs = [('a', 1),
         ('b', 2),
         ('c', 3), ]
#dic comprehension
dic = {key:value for key,value in pairs }
print(dic) #--> {'a': 1, 'b': 2, 'c': 3}

# example :
# dic --> list
dic = {'a': 1, 'b': 2, 'c': 3}
# create a list of (key, value) tuple called pairs
pairs=[]
for key,value in dic.items(): #--> items() function produce the tuple pairs.
    pairs.append((key,value))
print(pairs) #--> [('a', 1), ('b', 2), ('c', 3)]
# by using list comprehension
pairs= [(key,value) for key,value in dic.items()]
print(pairs) #--> [('a', 1), ('b', 2), ('c', 3)]

# set
# dic --> set
dic = {'a': 1, 'b': 2, 'c': 3}
keys = {key for key in dic}
print(f"the type of {keys} is {type(keys)}")
# --> the type of {'c', 'b', 'a'} is <class 'set'>
# a list of tuples --> set
pairs = [('a', 1),
         ('b', 2),
         ('c', 3), ]
s = {key for key, vaule in pairs}
print(s) #--> {'c', 'b', 'a'}

# comprehension--> filtering
# if statement
# example :
# create a list
# --> for loop
evens= []
for x in range(1_000_000+1):
    if x%2 == 0:
        evens.append(x)
print(evens[:10]) #--> [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
# --> list comprehension
evens= [x for x in range(1_000_000+1) if x%2==0]
print(evens[:10]) #--> [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# --> ⚠️there is no tuple comprehension in python.

# in-class exercise 2.1
lst = [2, 3, 10, 14, 20, 21, 25, 13, 15]
lst2= [x**2 for x in lst if x**2 > 150]
print(lst2) #--> [196, 400, 441, 625, 169, 225]
# in-class exercise 2.2
numbers=[0,1,1,2,5,6,8,2,4,6,8]
#--> use the set to unique values
lst =list({x for x in numbers if x%2==0}) #--> 直接将其用set转成list
print(lst) #-->[0, 2, 4, 6, 8]
# or
lst =[x for x in set(numbers) if x%2==0] #--> 先将numbers转成set，直接用于list
print(lst) #--> [0, 2, 4, 6, 8]
# sort() function --> make the numbers in ascending order by default.
lst.sort()
print(lst) #--> [0, 2, 4, 6, 8]

# 4. Modules and Packages
# create the yf_example1.py
# create the yf_example2.py
# --> documentation:
# Documentation is used to describe the use and functionality of modules, functions, classes, and methods.
# Docstrings are surrounded by triple quotes.(""" xxx """)
# Docstrings are easily available to functions like help .
# example:
def add(a,b):
    """ Returns the sum of two numbers """
    return a + b
help(add)
# output:
# Help on function add in module __main__:
# add(a, b)
# Returns the sum of two numbers
# help() to is generally used with python
#        interpreter console to get details about python objects
# --> comments:
# to explain the source code which are not obvious
# use "#" to comment a line of code

#--> Docstring styles
# there are different docstring styles
# each one has the specific guidelines
# the NumPy docstring is simple and widely used.
# to set the NumPy docstring style guideline in my Pycharm

#--> test cases and examples
# by using small examples inside the module containing the function
# example : in yf_example2.py module
# by a special variable : using _name_

#--> text, unicode and bytes
# method 1: DIR1 = 'C:\\User\\Someone'
# method 2: DIR2 = r'C:\User\Someone'

#--> access functionality from other modules
# create data directory( datadic) / data folder
# datadir ='/Users/zhouyaqi/PycharmProjects/toolkit/data'
#         --> data PyCharm location
#--> create modules
# ⚠️ toolkit_config.py
#--> create lecture packages
