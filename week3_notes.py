# WEEK 3
# Control flows
# 1. assignment statements and copies
# < target>= <expression>
# example 1:
Var1= 'a'
Var2= 'a'
Var3= 'a'
Var4= 'a'
# --> how many str instance with the value "a" are stored in the computer memory ?
# --> answer: only one !!! they have the same instance.
# example 2:
Var1= ['a']
Var2= ['a']
Var3= ['a']
Var4= ['a']
#--> answer: have 4 distinct list instances( mutable )in the computer memory!!!
#--> 4 different addresses of instance 'a'
lst1= ['a']
print(f"this is lst1:{lst1}")
lst2= ['b', lst1]
print(lst2) #--> ['b', ['a']]
lst2[1].append('c')
print("this is lst1 after modifying lst2: {}".format(lst1))
# --> this is lst1 after modifying lst2: ['a', 'c']
lst1= ['a']
lst3= ['b',['a']]
print(lst3) #--> ['b', ['a']]
lst3[1].append('c')
print(f"this is lst1 after modifying lst3: {lst1}")
# --> this is lst1 after modifying lst3: ['a'] !!!!!

# 2. Control flow !!!
# 2.1 control flow 1--> if statement
# if logical_expression:
#    statement a
#    statement b
# example 1:
happy = False
if happy is True: #--> 'is' operator will test if 2 instances are the same
    print("I am happy")
print (" this will print regardless of the value of happy ")
#--> this will print regardless of the value of happy
# 4 white spaces to intend code block
happy = True
very_happy = True
if happy is True:
    print("I am happy") #--> 4 spaces
    if very_happy is True: #--> 4 spaces
        print("Actually, I'm really happy!") #--> 8 spaces
# Truthy/ Falsy is just bad-y
#Python does not require that you use Boolean values inside if statements
happy = True
if happy:
    print("I am happy") #--> I am happy
happy = 10
if happy:
    print("I am happy") #--> I am happy
# What values are Truthy and what values are Falsy in Python?
# Falsy:
# None
# False
# 0 numerical values
# Empty strings and empty containers from the standard library (list, dict, tuple, set)
# Truthy:
# All other standard types are treated as True.


#comparison operators
# compare a and b
# a equals b      --> a == b
# a not equals b  --> a != b
# a strictly less than b --> a < b
# a less than or equal to b --> a <= b
# a strictly greater than b --> a > b
# a greater than or equal to b --> a >= b

# " '==' and 'is' are not equivalent
# '==' is the equality operator
# '==' operator will compare the value of 2 objects
# 'is' is the identity operator
# 'is' compares if the objects correspond to the same instance in the computer memory.
# example :
var1 = 'a'
var2 = 'a'
print(var1 is var2) # --> True
print(var1 == var2) # --> True

var3 = ['a']
var4 = ['a']
print(var3 is var4) # --> False
print(var3 == var4) # --> True

# ??Use is only to test if something is either None , True , or False. For everything else, use ==

# the else statement, when if condition is not met
b = False
if b is True:
    print("b is True")
else:
    print("b is not true")
# --> "b is not true"

# the elif statement
# if , elif (else if) and else statement are at the same indentation level, which is treated as a group
a = 0
b = True
if a != 0:
    print(" a is non-zero")
elif b is True:
    print("b is true")
elif a <0 and b is True:
    print("a is negative and b is true")
else:
    print(" None of the condition above hold")
# --> " b is true"
# example 2: when the first if statement is satisified and any conditions met later will not be executed.
a = 0
b = True
if a == 0:
    print(" a is zero")
elif b is True:
    print("b is true")
elif a <0 and b is True:
    print("a is negative and b is true")
else:
    print(" None of the condition above hold")
# --> "a is zero"
# pass statement : as a placeholder when developing code
# example 3:
happy = True
if happy is True:
    pass #--> nothing will happen
# example 4
if x > 0 and y is True:
# Write code for this case later
pass
elif x <= 0 and y is True:
# Write code for this case later
pass
else:
# Write code for this case later
pass

# input() function
name= input('who are you?')
print("welcome to the class,",name)
#--> "who are you?"
# input (prompt)
# the input() function returns a string

# in-class exercise 1
hours = input('enter number of hours you worked this week:')
#Python 3 output numeric value as a string in input () function
hours = int(hours) # --> convert string to integer by using int() function
# --> improvement !!! the hours maybe not integer and it can be 2.5 hours or other.
#     so can int()--> float()
normal_rate = 51.45
overload_rate = 88.9
# improvement !!! PEP 8 - Style Guide for Python Code
if hours > 35:
    pay = (35* noraml_rate)+ (hours - 35)* overload_rate
else:
    pay = hours * normal_rate
print(f"this weekly payment is: {pay} ")

# 2.2 control flow 2--> Loops
# Loops allow us to execute code multiple times, changing key variables on each execution.
# loop constructure has 2 statements : for statement (more popular) and while statement
# --> for statement
letter_lst= ['a','b','c','d']
for letter in letter_lst:
    print(letter) #--> a
#                      b
#                      c
#                      d
import yfinance
start = '2020-01-01'
end = None
tickers = ["QAN.AX", "WES.AX"]
for tic in tickers:
# download the ticker data from yfinance
    df = yfinance.download(tic, start, end, ignore_tz=True)
    print(df)
# Get the base name of the ticker
# E.g. QAN.AX -> qan
tic_base = tic.lower().split('.')[0]
# Save data to a csv file named after tic_base
df.to_csv(f'{tic_base}_stk_prc.csv')

# loops --> tuples
# tuple is iterable
# example
for v in ("string", True, 1):
    print(v) # -->string
#                 True
#                 1

# loops--> sets
# to make sure each object analysed once if we make a mistake and add a stock to the set twice:
s =set()
s.add("QAN.AX")
s.add("QAN.AX")
s.add("WES.AX")
for tic in s:
    print(tic) #--> WES.AX
#                   QAN.AX

# loops --> dictionaries
# 3 methods for looping : keys ; values ; both kays ad values simultaneously (as a pair)
# First, looping over keys is the default. On each pass, Python picks a different key to assign to the loop variable.
d = { "beauty": True,
      "truth": True,
      "red wheelbarrow": 100000,
      5: "fingers", }
for key in d:
    print(key)
# second, loop over the values by using values dictionary method
d = { "beauty": True,
      "truth": True,
      "red wheelbarrow": 100000,
      5: "fingers", }
for val in d.values(): #--> values() function
    print(val)
# third, loop over a tuple packing the key-value pair as (key, value) by using items method
d = { "beauty": True,
      "truth": True,
      "red wheelbarrow": 100000,
      5: "fingers", }
for key_value_tuple in d.items():
    print(f"key_value_tuple is {key_value_tuple}")
# unpacking --> a tuple
    (key, value)= key_value_tuple
    print("key:{}, value:{}".format(key, value))
# or you can simply unpack the tuple at the beginning of the loop
d = { "beauty": True,
      "truth": True,
      "red wheelbarrow": 100000,
      5: "fingers", }
for key, value in d.items():
    print(f"key:{key},value:{value}")
#Caution:
# As with sets, do not expect to receive the keys or values in any specific order when looping over dictionaries.
# conceptually, dic is an unordered container.

# loops--> range
# by using the built-in range function to generate many objects: e.g. lst[0:1000]
for i in range(0, 5): # or range(0,5,1) or range(5)
    print(f"i is now {i}")
# step : 指的是每个object之间的序列增量
for even in range(0, 10, 2): # count over even numbers by setting the step of 2
    print(even)
# the step can be negative
for i in range(5,-1,-1):
    print("This message will self-destruct in {} secs...".format(i))

# loops--> enumerations --> give an index
# Keeping track of the iteration number as we progress through an iterable.
letters =['a','b','c','d','e']
i = 0
for x in letters:
    print(f"letters[{i}]--> {x}")
    i += 1 # --> or i= i+1
# output :
# letters[0]--> a
# letters[1]--> b
# letters[2]--> c
# letters[3]--> d
# letters[4]--> e
# by using enumerate() function
# the returned iterable consists of tuples( i, ele)
letters= ['a','b','c','d','e']
for tup in enumerate(letters):
    print(tup)
# output:
# (0, 'a')
# (1, 'b')
# (2, 'c')
# (3, 'd')
# (4, 'e')
# or unpack the tuples
letters= ['a','b','c','d','e']
for i, ele in enumerate(letters):
    print(f"letters[{i}] --> {ele}")
# output :
# letters[0]--> a
# letters[1]--> b
# letters[2]--> c
# letters[3]--> d
# letters[4]--> e

# enumerate()--> dictionary
d= { "beauty": True,
     "truth": True,
     "red wheelbarrow": 100000,
     5: "fingers",}
for i, ele in enumerate(d.items()):
    print(f'iteration{i} gives {ele}')
# output:
# iteration0 gives ('beauty', True)
# iteration1 gives ('truth', True)
# iteration2 gives ('red wheelbarrow', 100000)
# iteration3 gives (5, 'fingers')
# ??? dic is unordered ??

# in-class exercise 2
numbers = [3, 9, 1, 5, 7, 2, 11, 0, 3, 12, 3, 15]
temp_largest = numbers[0]
for number in numbers:
    if number > temp_largest:
        temp_largest = number
    print(number, temp_largest)
print(f'the largest value is {temp_largest}')
# or the simple solution by using max() function
numbers = [3, 9, 1, 5, 7, 2, 11, 0, 3, 12, 3, 15]
largest = max(numbers)
print('the largest number is {}'. format(largest))

# ---> while statement
# convert the for statement to while statement
# example:
the_sum = 0
for i in range(1,101):
    the_sum= the_sum+i
print(the_sum) #--> 5050
#--> a while loop
the_sum=0
i=1
while i<=100:
    the_sum= the_sum + i
    i += 1
print(the_sum) #--> 5050

# disadvantages of while loops :
# Can accidentally construct loops that will run forever and it called infinite loop.
x = 0.1
while x != 1.1:
    x += 0.1
print(x)
#??? how to express a range but not all numbers are integer???

# Nested structures and conditional statements
# example :
years = [2018, 2019,2020]
months = ["Jan",
          "Feb",
          "Mar",
          "Apr",
          "May",
          "Jun",
          "Jul",
          "Aug",
          "Sep",
          "Oct",
          "Nov",
          "Dec", ]
for year in years:
    for month in months:
        print (f"'year': {year}, 'month': {month}")
# nested structure can mix for and while loop
#in-class exercise 3
lst1 = [1,2,3]
lst2 = [1,2,3]
for i in lst1:
    for x in lst2:
        print (i,x) # --> ❌ 因为会出现好几对重复的数对
        if i<= x:
            print(i,x) #--> ☑️正确的！！！

# Additional looping control-->  continue and break
# to skip a particular loop iteration or exit a loop before it is complete
# the continue and break statements apply to the active and innermost loop
# continue statement :
# to stop evaluating a particular iteration in a loop and proceeds to the next iteration.
# example:
the_sum_evens= 0
for x in range(0,101):
    if x % 2 == 0:
        the_sum_evens = the_sum_evens + x
print(f'the sum of evens is {the_sum_evens}') #--> the sum of evens is 2550

the_sum_evens= 0
for x in range(0,101,2):
    the_sum_evens= the_sum_evens + x
print(the_sum_evens) #--> 2550
#⚠️ 注意print 的位置可能会导致不同的结果
# by using continue statement to ignore the odd numbers
the_sum_evens= 0
for x in range(0,101):
    print (f'loop is on {x}')
    if x %2 ==1: #--> x is odd
        continue #--> only proceed if the number is even and ignore/ stop when x is odd.
    print(f'summing the value of {x}') #--> x is even
    the_sum_evens = the_sum_evens + x
print('sum of evens is {}'.format(the_sum_evens))
# The advantage / purpose of continue statement :
# Embedding a lot of code inside if statements can make programs hard to read.
# continue statements can make code more elegant by eliminating deep indentation.
# the continue statement can help you improve your code readability and maintainability.
# example :
the_sum= 0
for x in range(0,101):
    if x %2 == 0:
        continue
    if x % 3 == 0:
        continue
    if x % 7 == 0:
        continue
    if x %13 == 0:
        continue
    the_sum = the_sum + x
print(the_sum) #--> 1296
# or :
the_sum= 0
for x in range(0,101):
    if x %2==0 and x%3==0 and x%7==0 and x%13==0:
        continue
    the_sum= the_sum + x
print(the_sum) #--> 5050 ??? ❌❓
the_sum= 0
for x in range(0,101):
    if x %2==0 and x%3==0 and x%7==0 and x%13==0:
        continue
        the_sum= the_sum + x
print(the_sum) #--> 0 ❌❓

the_sum= 0
for x in range(0,101):
    if x %2!=0 and x%3!=0 and x%7!=0 and x%13!=0:
        the_sum= the_sum + x
print(the_sum) #--> 1296

# break statement :
# The break statement will exit a loop immediately.
# This can be useful in a number of situations in both for and while loops.
# example: Fibonnacci sequence
fib_current= 1
fib_prior = 0
while fib_current < 10000: # 为什么不能小于等于10000
    print(f'fibonacci value is {fib_current}')
    fib_current, fib_prior= fib_current + fib_prior, fib_current
print(f'the first fibonacci value greater than 10000 is {fib_current}')
# --> 10946
# by using a break statement
fib_current= 1
fib_prior = 0
while True:
    print (f'fibonacci value is {fib_current}')
    fib_current, fib_prior = fib_current + fib_prior, fib_current
    if fib_current >= 10000:
        break
print(f'the first fibonacci value greater than 10000 is {fib_current}')
#--> 10946
# outer loop and inner loop
# example :
for x in range(0, 4): #--> outer loop
    for y in range(0,4): #--> inner loop,continuing to next y value
        if x + y >= 4:
            continue #-->continuing to next y value
        elif (x + y) % 2 != 0:
            continue #--> continuing to next y value
        print(f"x = {x} and y = {y} have even sum less than 4")
# output:
# x = 0 and y = 0 have even sum less than 4
# x = 0 and y = 2 have even sum less than 4
# x = 1 and y = 1 have even sum less than 4
# x = 2 and y = 0 have even sum less than 4

# example : to eliminate the possibility of y> x
for x in range(0,4):
    for y in range(0,4):
        if y > x:
            break
        elif x+y >= 4:
            continue
        elif (x+y) %2 != 0: #--> ⚠️x+y 要用（）括起来，否则得不到正确的结果
            continue
        print(f"x= {x} and y={y} have the sum lees than 4 ")
#example1 :
for even in range (0,10,2):
    print(even)
    if even > 2:
        break
# output: 0,2,4 --> 因为4>2,所以当4被printed后，这个loop就停止了.
#example 2:
for odd in range(1,10,2): #--> outer loop
    for even in range(0,10,2): #--> inner loop
        if even > 2:
            break
    print(even, odd) #--> 4 1
#                         4 3
#                         4 5
#                         4 7
#                         4 9

for even in range(0,10,2): #--> inner loop
    if even > 2:
        break
    print(even) #--> 0,2 ⚠️注意print的位置
print(even) #--> 4  ⚠️注意print的位置 -->
# The print statement is outside the inner loop. This means the inner loop will finish before the first print statement.
# example 3 :
for even in range(0,10,2):
    print(even)
    if even >2:
        continue
# output: 0,2,4,6,8
#在此处，continue statement 是无关紧要的，所有elements都被printed.

#example 4:
for even in range(0,10,2):
    if even >2:
        continue
    print(even) #--> 0,2
print(even) #-->8 # ❌❓
