class Employee:
	raise_with = 8/100

	total_employees = 0

	def __init__(self, first, last, age, pay):
		self.first_name = first
		self.last_name = last
		self.age = age
		self.salary = pay

		Employee.total_employees +=1

	def fullName(self):
		return self.first_name +" "+ self.last_name

	def fullDetails(self):
		return f"Hi {self.fullName()} as per our record you are {self.age} years old and your pay is {self.salary}."

	def raisePay(self):
		raisepay = self.salary * self.raise_with
		return f"Your salary has been incremented with {raisepay} amount"

	@classmethod
	def classPay(cls):
		clsname = cls.__name__
		return f"Name of the class is {clsname}. | Example of @classmethod"


	@staticmethod
	def staticPay():
		static = 5
		return f"Print value of the variable {static}. | Example of @staticmethod"


emp1=Employee("Ram", "Tej", 38, 10000)
emp2 = Employee("Rishi", "Kapoor", 28, 10000)
emp3 = Employee("Foo", "Bar", 25, 10000)

print(emp1.classPay())
print(emp2.staticPay())

"""
if you want to work with instance of class use normal function with self
example:
def normal(self):
	pass

if you wish to work with class and attributes use classmethod
example:
@classmethod
def clsmethod(cls):
	pass

if you wish to work with static values use staticmethod
example:
@staticmethod
def stcmethod():
	pass
"""
