# class MyAClass:

# 	def __init__(self, *args):
# 		self.dataA = args
		# self.dataB = kwargs

	# def print_data(self):
	# 	print(self.dataA)

	# def print__data(self):
	# 	print(self.dataB)


# class1 = MyAClass("test", "test", "test")

# class1.print_data()

# class1.print__data()

# class MyBClass:

# 	def __init__(self, **kwargs):
# 		self.dataA = kwargs
		# self.dataA = kwargs["test"]
		# self.dataB = kwargs

# 	def print_data(self):
# 		print(self.dataA)

# data = {"test":"data", "test2":"data2", "test3":"data3"}

# class2 = MyBClass(**{"test":"data"})

# class2 = MyBClass(**data)

# class2.print_data()



# class NewAClass(MyAClass):

# 	# override test
# 	def print_data(self):
# 		print("this is _data override")

# 	def print__data(self):
# 		super().print__data()
# 		# print(dataa)
# 		print("this is __data override")

	# def print__data(self):
	# 	print("this is __data override")


# class2 = NewAClass(["test3","test4"], {"key2":"value3", "key3":"value4"})

# class2.print_data()

# class2.print__data()
print("*"*50+"New Class"+"*"*50)

class MyClass:

	def __init__(self, *args, **kwargs):
		self.dataA = args
		self.dataB = kwargs

	def print_data(self):
		print(self.dataA)

	def print__data(self):
		print(self.dataB)

classA = MyClass(["data0", "data1", "data2"], **{"key0":"val0","key1":"val1","key2":"val2"})

classA.print_data()

classA.print__data()

print("*"*50+"New Class"+"*"*50)

class NewClass(MyClass):

	def print_data(self):
		print("this is _data override")

	def print__data(self):
		super(NewClass, self).print__data()
		print("this is __data override")

classB = NewClass(["data3", "data4", "data5"], **{"key3":"val3","key4":"val4","key5":"val5"})

classB.print_data()

classB.print__data()

print("*"*50+"New Class"+"*"*50)

class NewClassA:

	def __init__(self, *args, **kwargs):
		self._data = args
		self.__data = kwargs


	def print_data(self):
		for _data in self._data:
			print(_data)

	def print__data(self):
		for _key, _val in self.__data.items():
			print("{} {}".format(_key, _val))


classC = NewClassA(["data3", "data4", "data5"], **{"key3":"val3","key4":"val4","key5":"val5"})

classC.print_data()

classC.print__data()

print("*"*50+"New Class"+"*"*50)

class NewClassB(MyClass):

	def print_data(self):
		for _data in self.dataA:
			print(_data)

	def print__data(self):
		super(NewClassB, self).print__data()
		print("NewClassB")
		for _key, _val in self.dataB.items():
			print("{} {}".format(_key, _val))


classD = NewClassB(["data3", "data4", "data5"], **{"key10":"val10","key11":"val11","key12":"val12"})

classD.print_data()

classD.print__data()

print("*"*50+"New Class Testing super()."+"*"*50)

class NewClassC(NewClassB):

	def print_data(self):
		for _data in self.dataA:
			print(_data)

	def print__data(self):
		print("Before super")
		# super(NewClassB, self).print__data()
		print("After super")
		for _key, _val in self.dataB.items():
			print("{} {}".format(_key, _val))
		super(NewClassC, self).print__data()


classE = NewClassC(["data3", "data4", "data5"], **{"key3":"val3","key4":"val4","key5":"val5"})

classE.print_data()

classE.print__data()