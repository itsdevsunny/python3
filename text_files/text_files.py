file_path = ""

file_name = ""

file_log = "error.log"

content = "This is test content."

error_log = "File name not defined"

if file_name != "":
	with open(file_path+file_name, "w") as file:
		print(content, file=file)
else:
	with open(file_path+file_log, "a") as file:
		print(error_log, file=file)