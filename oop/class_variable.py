class Employee:
	# class variable are variables that are shared amongst all instance.
	raise_with = 8/100

	total_employees = 0

	def __init__(self, first, last, age, pay):
		self.first_name = first
		self.last_name = last
		self.age = age
		self.salary = pay

		# self.total_employees +=1 #this will override value each time
		Employee.total_employees +=1

	def fullName(self):
		return self.first_name +" "+ self.last_name

	def fullDetails(self):
		return f"Hi {self.fullName()} as per our record you are {self.age} years old and your pay is {self.salary}."

	def raisePay(self):
		# raisepay = self.salary * Employee.raise_with # this will raise salary as per class
		raisepay = self.salary * self.raise_with # this will raise salary as set in an instance
		return f"Your salary has been incremented with {raisepay} amount"

emp1=Employee("Ram", "Tej", 38, 10000)
emp2 = Employee("Rishi", "Kapoor", 28, 10000)
emp3 = Employee("Foo", "Bar", 25, 10000)

# print(Employee.fullDetails(emp1))
# print(Employee.fullDetails(emp2))
# print(Employee.fullDetails(emp3))

emp1.raise_with = 3/100
emp2.raise_with = 10/100

# print(Employee.__dict__)
# print(emp1.__dict__)
# print(emp2.__dict__)
# print(emp3.__dict__)

print(Employee.raisePay(emp1))
print(Employee.raisePay(emp2))
print(Employee.raisePay(emp3))

#this will return raise_with as value set by an instance if any otherwise default as per class
print(emp1.raise_with)
print(emp2.raise_with)
print(emp3.raise_with)

# print(Employee.total_employees)
# print(emp1.total_employees)
# print(emp2.total_employees)
# print(emp3.total_employees)

