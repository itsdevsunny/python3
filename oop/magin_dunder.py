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

	def __repr__(self):
		return f'{self.__class__}({self.first_name}, {self.last_name}, {self.salary})'

	def __str__(self):
		return self.full_name()

	def __add__(self, other):
		return self.salary + other.salary


emp1=Employee("Foo", "Bar", 10000)

emp2=Employee("Foo", "Bar", 10000)

print(emp1.full_name())

emp1.raise_sal = 1.5

emp1.raise_sala()

print(Employee.raise_sal)

print(emp1.raise_sal)

print(emp1)

print(dir(Employee))

print(emp1 + emp2)

print(emp1 + emp2)