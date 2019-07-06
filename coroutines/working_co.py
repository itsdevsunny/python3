import asyncio


async def main():
	print('hello')
	await asyncio.sleep(1)
	print('world')

asyncio.run(main())


# >>> x = False
# >>> 
# >>> y = True
# >>> 
# >>> if x:
# ...     print("x is false")
# ... 
# >>> 
# >>> def checks(a):
# ...     if a:
# ...             print(f'{a} is true')
# ...     else:
# ...             print(f'{a} is false')
# ... 
# >>> 
# >>> checks(x)
# False is false
# >>> 
# >>> checks(y)
# True is true
# >>> 
# >>> checks(not y)
# False is false
# >>> 
# >>> checks(not x)
# True is true
# >>> 
