class Employee:
	hike = 1.10

	def __init__(self, name, age, salary):
		self.name = name
		self.age = age
		self.salary = int(salary)

	def intrduction(self):
		return f"Hi my name is {self.name} and my age is {self.age}."

	def salary_package(self):
		return f"My salary package is {self.salary}."

	def salary_hike(self):
		return (self.salary * self.hike)


a = Employee('ethan hunt', '38', '1000')
a.hike=1.60
print(a.intrduction())
print(a.salary_package())
print(a.salary_hike())

class Accounts(Employee):
	hike = 1.30 # after inheritace any change in the class variable would reflect every where except 
				# instace of that class sould not be chagned for that instance

b = Accounts('ethan hunt', '38', '1000')
b.hike=1.20
print(b.intrduction())
print(b.salary_package())
print(b.salary_hike())

c = Accounts("john wick", '30', '2000')
print(c.intrduction())
print(c.salary_package())
print(c.salary_hike())

d = Employee('ethan hunt', '38', '1000')
d.hike=1.50
print(d.intrduction())
print(d.salary_package())
print(d.salary_hike())


''' A) if you have a class Employee that has a class variable hike if any change is made to class
variable in the instance of that class would not reflect in the class at all.

B) Any change made after inheritance of that would reflect only to that class and its instance
if instance of that has not change that varible for itself.
'''