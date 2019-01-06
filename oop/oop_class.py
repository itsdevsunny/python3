class Employee:

	def __init__(self, first, last, age):
		self.first_name = first
		self.last_name = last
		self.age = age
		# self.full_name = self.first_name + " " + self.last_name
		# self.full_name = first + " " + last

	def fullName(self):
		return self.first_name +" "+ self.last_name

	def fullDetails(self):
		# self.full_name = self.first_name + self.last_name
		# return "Hi {} as per our record you are {} years old.".format(self.full_name, self.age)
		# return f"Hi {self.full_name} as per our record you are {self.age} years old."
		return f"Hi {self.fullName()} as per our record you are {self.age} years old."


emp1=Employee("Ram", "Tej", 38)

# print(emp1.fullDetails())		

emp2 = Employee("Rishi", "Kapoor", 28)

print(Employee.fullDetails(emp1))
print(Employee.fullDetails(emp2))