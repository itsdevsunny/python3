# Normal string
string = "Hello World!"

print(string)

# Escaping string

string1 = "There is a saying : \"Every Dog has it's Day\""

print(string1)

string3 = 'This is example of single quote escaping quote. It\'s is every where.'

print(string3)

# example of format string 

string4 = "This is {} example of format string {}".format("a", ".")

print(string4)

"""
this is a multiline comment examle 

this format sting is quite awsome simple place the variable in number and use according 
to their place.

"""

string5 = "awsome"

string6 = "this"

string7 = "{1} example is also {0} {1} looks {0}".format(string5, string6)

print(string7)

# this is illustrates how you use value from dictionary and list

dictionary = {"name":"John Doe", "age":"35"}

this_list = ["Travis", "40"]

string8 = "{} is {} year old".format(dictionary["name"], dictionary["age"])

print(string8)

string9 = "{0} is {1} year old".format(dictionary["name"], dictionary["age"])

print(string9)

string10 = "{0[name]} is {1[age]} year old".format(dictionary, dictionary)

print(string10)

string11 = "{0[name]} is {0[age]} year old".format(dictionary)

print(string11)

string12 = "{0[0]} is {0[1]} year old".format(this_list)

print(string12)

class Person():
	def __init__(self, name, age):
		self.name = name
		self.age = age

person1 = Person("Delta", "25")

string13 = "{0.name} is {0.age} year old".format(person1)

print(string13)

#print dictionary values 

dictionary1 = {"name":"Jenn", "age":"30"}

string14 = "{name} is {age} year old".format(**dictionary1)

print(string14)

string15 = "{name} is {age} year old".format(name="Pie", age="6")

print(string15)

# this is called formatting number place

for i in range(10):
	print("Value is {:02}".format(i))

pi=3.148956

string16 = "Value of pi is {:.2f}".format(pi)

print(string16)

mb = 1000000

string17 = "Value of 1mb is {:,.2f}".format(mb)

print(string17)

import datetime

my_date = datetime.datetime(2018, 12, 31, 4, 55, 45)

string18 = "this is example of datetime format {}".format(my_date)

print(string18)

string19 = "this is example of datetime format {:%B %d, %Y}".format(my_date)

print(string19)


string20 = "today is {0:%d}st and year is {0:%Y} day of the year is {0:%j}".format(my_date)

print(string20)

#f is new and is introduced after python 3.6

greet = "Hello"

name = "Kulfi"

string21 = f"{greet} {name.upper()} welcome"

print(string21)