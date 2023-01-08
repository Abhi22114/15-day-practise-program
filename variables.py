# variables data types

# variables are containers for storing data values
# pyhton has no command for decalring a varriable 
name="Abhijeet"  #(for storing string we use single and double quotes)
print(name)
age=18
section="KOC09"
print(name,age,section)

print(name + section)
# , is used when we have to print more than 1 varribles in a lines
#  + is also used but incase of string only
# , adds a space at the end but + donot add space 


# RULES OF VARRIABLes in python

#1. variables name can only starts with letters,underscore
#2. variables name cannot start with number 
#3. variables can contain alphabets or underscore 
#4. A variable name can only contain alpha-numeric characters and 
#    underscores (A-z, 0-9, and _ )

# Camel Case
# Each word, except the first, starts with a capital letter:
myFirstName = "John"

# Pascal Case
# Each word starts with a capital letter:
MyFirstName = "John"

# Snake Case
# Each word is separated by an underscore character:
my_first_name = "John"

#_abc123="abhijeet"
# name="abhijeet"




# variables in pyhton are case-sensitive
# examples-:
l="abhijeet"
L=18
print(l)
print(L)
# l will not over write on L


# how to change the types of varriables 
#  to specify the datatypes of a variable we use casting
a=15
print(type(a))
print(str(a))
print(float(a))

# Unpack a Collection
# when we have a collection of values in a list, tuple etc.
#  Python allows you to extract the values into variables. This is called unpacking.

# Example
My_Friends_Names= ["Dhoni", "Raja", "Vedant"]
x, y, z = My_Friends_Names
print(x)
print(y)
print(z)

