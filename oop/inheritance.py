class Employee:

	raise_sal = 1.04

	def __init__(self, first, last, salary):
		self.first_name = first
		self.last_name = last
		self.salary = salary

	def full_name(self):
		return self.first_name +" "+ self.last_name
		# return '{} {}'.format(self.first_name, self.last_name)	

	def full_details(self):
		# return f"Hi my name is {self.fullName()} and my salary package is Rs.{self.salary}."
		print(f"Hi my name is {self.full_name()} and my salary package is Rs.{self.salary}.")


	def raise_sala(self):
		self.salary = self.salary * self.raise_sal
		# return self.salary	
		# return f"My recent salary raise is {self.salary}."
		print(f"My recent salary raise is {self.salary}.")

	@staticmethod
	def test_me(data):
		print(f"{data}")

	@classmethod
	def test_cls(cls):
		print(f'I am called from {cls.__name__}')


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
			print("-->", emp.full_name())


if __name__=="__main__":
	emp1 = Employee("Ram", "Tej", 10000)
	emp2 = Developer("Rishi", "Kapoor", 10000, "Python")
	emp3 = Manager("Foo", "Bar", 10000, [emp2])
	emp3.add_emp(emp1)
	emp3.print_emp()
	emp3.raise_sal = 1.6
	emp3.raise_sala()
	emp2.raise_sala()
	emp3.test_me("sdfsafd")
	emp1.test_cls()
	emp2.test_cls()
	emp3.test_cls()