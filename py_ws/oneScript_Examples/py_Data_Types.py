"""
 ******************************************************************************
 * @author     : Jabed-Akhtar (github)
 * @Created on : 03.09.2022
 ******************************************************************************
 * @file       : py_Data_Types.py
 * @brief      : ---
 ******************************************************************************
 * :Steps      :
 *      1. ---
 * :Descriptions/Infos:
 *      - ---
 ******************************************************************************
"""


#Integers =====================================================================
a_int = 12
print(type(a_int))

#Floating point numbers ====================================================================
a_float = 4.2
print(type(a_float))
a_float_2 = 1.7e2
print('---> Value of variable a_float_2 is:', a_float_2, ', having data type:', type(a_float_2))

#Strings ======================================================================
a_str = "I am a string with '!"
print(a_str)
print(type(a_str))
print('\u2192') # unicode character with 16-bit hex value
# Raw strings
print('foo\nbar')
print(r'foo\nbar')
print('foo\\bar')
print(R'foo\\bar')
# Triple-Quaoted Strings
print('''This string has a single (') and a double (") quote.''')
print("""This is a
string that spans
across several lines""")

#Boolean Type, Boolean Context, and "Truthiness" ==============================
a_bool = True
print(type(a_bool))

#Composite Data Type > bytearray ==============================================
"""
- Creates and returns an object of the bytearray class
- description:
    |- The bytearray() method returns a bytearray object which is an array of the given bytes.
"""
a_num = [2, 3, 4, 5, 17]
# converting lost to bytearray
a_bytearray = bytearray(a_num)
print(a_bytearray)

#Composite Data Type > bytes ==================================================
"""
- Creates and returns a bytes object (similar to bytearray, but immutable)
- description:
    |- The bytes() method returns an immutable bytes object initialized with the given size and data.
"""
# Converting string to bytes *****
a_by_str = "This is a string."
# String with encoding 'utf-8'
a_arr = bytes(a_by_str, 'utf-8')
print(a_arr)
print(type(a_arr))
# Create a byte of integer size *****
a_by_int = 10
a_arr_int = bytes(a_by_int)
print(a_arr_int)
print(type(a_arr_int))
# Convert iterable list to bytes *****
rList = [1, 2, 3, 4, 5]
arr = bytes(rList)
print(arr)

#Composite Data Type > dict ===================================================
"""
- Creates a dict object
- description:
    |- Python dictionary is an unordered collection of items. Each item of a dictionary has a key/value pair.
    |- Dictionaries are optimized to retrieve values when the key is known.
"""

# empty dictionary
my_dict = {}
# dictionary with integer keys
my_dict = {1: 'apple', 2: 'ball'}
print(my_dict[2])
# dictionary with mixed keys
my_dict = {'name': 'John', 1: [2, 4, 3]}
print(my_dict[1])
# using dict()
my_dict = dict({1:'apple', 2:'ball'})
print(my_dict[2])
# from sequence having each item as a pair
my_dict = dict([(1,'apple'), (2,'ball')])
print(my_dict[2])
print(my_dict.get(1))
print(my_dict.get('address')) # because it doesn't exixt, it will return None
try:
    print(my_dict['address']) # because it doesn't exixt, it will return Error!!! -> use get() method
except:
    print("my_dict['address'] is not correct!")

# Creating new dictionary
squares_dict = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(squares_dict.pop(2)) # -> returns 4

#Composite Data Type > frozenset ==============================================
"""
- Creates a frozenset object
- description:
    |- The frozenset() function returns an immutable frozenset object initialized with elements from the given iterable.
    |- Frozen set is just an immutable version of a Python set object. While elements of a set can be modified at any time, elements of the frozen set remain the same after creation.
    |- Due to this, frozen sets can be used as keys in Dictionary or as elements of another set. But like sets, it is not ordered (the elements can be set at any index).
    |- The syntax of frozenset() function is: frozenset([iterable])
"""

# tuple of vowels
vowels = ('a', 'e', 'i', 'o', 'u')
fSet = frozenset(vowels)
print('The frozen set is:', fSet)
print('The empty frozen set is:', frozenset())
# frozensets are immutable
try:
    fSet.add('v')
except:
    print("fSet.add('v') is not possible!")

# Frozenset operations *****
# initialize A and B
A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])
# copying a frozenset
C = A.copy()  # Output: frozenset({1, 2, 3, 4})
print(C)
# union
print(A.union(B))  # Output: frozenset({1, 2, 3, 4, 5, 6})
# intersection
print(A.intersection(B))  # Output: frozenset({3, 4})
# difference
print(A.difference(B))  # Output: frozenset({1, 2})
# symmetric_difference
print(A.symmetric_difference(B))  # Output: frozenset({1, 2, 5, 6})

C = frozenset([5, 6])
# isdisjoint() method
print(A.isdisjoint(C))  # Output: True
# issubset() method
print(C.issubset(B))  # Output: True
# issuperset() method
print(B.issuperset(C))  # Output: True

#Composite Data Type > list ===================================================
"""
- Creates a list object
- description:
    |- Python List methods: append(), extend(), insert(), remove(), pop(), clear(), index(), count(), sort(), reverse(), copy()
"""
a_list = [1, 2, 3, 4] # list of integers
b_list = [1, "Hello", 3.4] # list with mixed data types
c_list = [] # an empty list
d_list = ["mouse", [8, 4, 6], ['a']] # nested list
print(d_list[1][0]) # -> 8
# negative indexing
print(b_list[-1])
# List slicing
print(a_list[0:2]) # printing numbers from 0 to 1st position
print(a_list[2:]) # printing numbers from 2th to last position
# changing value inside list
b_list[1] = 'Hi'
print(b_list)
# Appending value to list
b_list.append(25)
print(b_list)
# using + oprator to add two lists
e_list = a_list + b_list
print(e_list)
print(b_list * 3) # repeats list 3 times
# inserting number
b_list.insert(1, 'new item')
print(b_list)
# deleting an item
del b_list[1]
print(b_list)

#Composite Data Type > object/Class ===========================================
"""
- Creates a new featureless object
"""

class Person:
    "This is a person class"
    age = 10

    def greet(self):
        print('Hello')

# Output: 10
print(Person.age)
# Output: <function Person.greet>
print(Person.greet)
# Output: "This is a person class"
print(Person.__doc__)

# Creating an Object
newObj = Person()
newObj.greet()

# Constructors
newObj2 = Person()
newObj2.dob = "27th Dec"
print(newObj2.age, '-', newObj2.dob)
# deleting attributes
del newObj2.dob
try:
    print(newObj2.age, '-', newObj2.dob)
except:
    print("newObj2.dob doesn't exist.")

#Composite Data Type > set ====================================================
"""
- Creates a set object
- A set is an unordered collection of items. Every set element is unique (no duplicates) and must be immutable (cannot be changed).
- However, a set itself is mutable. We can add or remove items from it.
- Sets can also be used to perform mathematical set operations like union, intersection, symmetric difference, etc.
"""

# set of integers
my_set = {1, 2, 3}
print(my_set)
# set of mixed datatypes
my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)

# Difference between disctionary and set
# initialize a with {}
a = {}
# check data type of a
print(type(a)) # -> dict
# initialize a with set()
a = set()
# check data type of a
print(type(a)) # -> set

# modifying set
my_set = {1, 3}
print(my_set)
my_set.add(2)
print(my_set)
my_set.update([2, 3, 4])
print(my_set)
my_set.update([4, 5], {1, 6, 8})
print(my_set)

# removing elements from a set
# initialize my_set
my_set = {1, 3, 4, 5, 6}
print(my_set)
# discard an element
my_set.discard(4)
print(my_set) # Output: {1, 3, 5, 6}
# remove an element
my_set.remove(6)
print(my_set) # Output: {1, 3, 5}
# discard an element, which is not present
my_set.discard(2)
print(my_set) # not present in my_set -> Output: {1, 3, 5}
# remove an element | not present in my_set
try:
    my_set.remove(2) # -> you will get an error.
except:
    print('remove option is not present for set!')

# clear my_set
# Output: set()
my_set.clear()
print(my_set)


#Composite Data Type > tuple ==================================================
"""
Creates a tuple object
"""
# TBD

# ****************************** END OF FILE **********************************