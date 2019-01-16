def test(v):
	word = "def"
	if not v % 3 != 0 and not v % 5 != 0:
		word = "foo"
	elif not v % 3 != 0:
		word = "bar"
	elif not v % 5 != 0:
		word = "foo bar"
	return word


for i in range(1,20):
	test(i)



# def read(v):
# 	try:
# 		print(v)
# 	Except test:

# 	else:
# 		print(v)
# 	Except :
# 		pass

# lp = "C:/Users/DELL/Desktop/cordova/dirpy/dirpy4"

x, y = 1, 0

#  will through error

# try:
# 	result = x / y
# else:
# 	print("result is", result)
# except SyntaxError:
# 	print("SyntaxError this!")
# except ZeroDivisionError:
# 	print("division by zero!")
# finally:
# 	print("executing finally clause")


try:
	result = x / y
except ZeroDivisionError:
	print("division by zero!")
else:
	print("result is", result)
finally:
	print("executing finally clause")