class Employee:

	raise_sal = 1.04

	def __init__(self, first, last, salary):
		self.first_name = first
		self.last_name = last
		self.salary = salary

	def fullName(self):
		return self.first_name +" "+ self.last_name

	def fullDetails(self):
		return f"Hi my name is {self.fullName()} and my salary package is Rs.{self.salary}."

	def raiseSal(self):
		self.salary += self.salary* self.raise_sal
		return f"My recent salary raise is {self.salary}."


class Developer(Employee):
	raise_sal = 1.50

	def __init__(self, first, last, salary, prog):
		super().__init__(first, last, salary)
		self.prog = prog

class Manager(Employee):

	def __init__(self, first, last, salary, emps=None):
		super().__init__(first, last, salary)
		if emps is None:
			self.emps = []
		else:
			self.emps = emps

	def add_emp(self, emp):
		if emp not in self.emps:
			self.emps.append(emp)

	def remove_emp(self, emp):
		if emp in self.emps:
			self.emps.remove(emp)

	def print_emp(self):
		for emp in self.emps:
			print("-->", emp.fullName())

emp1 = Employee("Ram", "Tej", 10000)
emp2 = Developer("Rishi", "Kapoor", 10000, "Python")

emp3 = Manager("Foo", "Bar", 10000, [emp2])

print(emp3.first_name)
# print(emp3.add_emp([emp1]))
print(emp3.print_emp())