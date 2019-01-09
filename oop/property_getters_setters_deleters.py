class Employee:

	raise_sal = 1.04

	def __init__(self, first, last, salary):
		self.first_name = first
		self.last_name = last
		self.salary = salary

	def full_name(self):
		return self.first_name +" "+ self.last_name

	def full_details(self):
		print(f"Hi my name is {self.full_name()} and my salary package is Rs.{self.salary}.")


	def raise_sala(self):
		self.salary = self.salary * self.raise_sal
		print(f"My recent salary raise is {self.salary}.")


	@property
	def fullname(self):
		return f'{self.first_name} {self.last_name}'
	
	@fullname.setter
	def fullname(self, fullname):
		first, last = fullname.split(" ")
		self.first_name = first
		self.last_name = last

	@fullname.deleter
	def fullname(self):
		self.first_name = None
		self.last_name = None
		print("Deleting done!")

	def __repr__(self):
		return f'{self.__class__}({self.first_name}, {self.last_name}, {self.salary})'

	def __str__(self):
		return self.full_name()

	def __add__(self, other):
		return self.salary + other.salary


emp1=Employee("Foo", "Bar", 10000)

emp2=Employee("Foo1", "Bar1", 10000)

emp2.fullname = "Foo2 Bar2"

del emp1.fullname

print(emp1.fullname)
print(emp2.fullname)