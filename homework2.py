import csv

input_file = csv.DictReader(open("Condom_Distribution_Sites.csv"))

for row in input_file:
	print row
	