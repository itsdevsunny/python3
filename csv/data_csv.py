import csv

# with open('new_data.csv', 'r') as data_file:
# 	data_csv = csv.reader(data_file)

with open('data.csv', 'r') as data_file:
	data_csv = csv.DictReader(data_file)

# with open('new_data.csv', 'r') as data_file:
# 	data_csv = csv.reader(data_file, delimiter='\t')

	#next(data_csv)
	# with open('new_data.csv', 'w') as new_file:
	# 	csv_writer = csv.writer(new_file, delimiter='-')
	
	# with open('new_data.csv', 'w') as new_file:
	# 	csv_writer = csv.writer(new_file, delimiter='\t')	
	# 	for line in data_csv:
	# 		csv_writer.writerow(line)
	
	# for line in data_csv:
	# 	print(line['Name'])

	# for line in data_csv:
	# 	print(line)

	#print(data_csv)

	with open('new_data1.csv', 'w') as file2:
		field = ['Sr No','Name', 'Address', 'Occupation', 'State', 'Unit1', 'Unit2', 'Unit3', 'Unit4', 'Unit5' ]

		csv_write = csv.DictWriter(file2, fieldnames=field)
		csv_write.writeheader()

		for line in data_csv:
			# print(line)
			csv_write.writerow(line)


