import mod1

print("Imported mod2 -> mod1 {}".format(mod1))

print("Outside __main__ mod2 {}".format(__name__))

if __name__=="__main__":
	print(" If Inside __main__ mod2")
else:
	print("Else Inside __main__ mod2")