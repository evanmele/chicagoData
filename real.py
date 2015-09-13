import csv


with open('disease1.csv', 'rb') as csvfile:
	
	spamreader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
	spamreader.next()
	
	for row in spamreader:
			print row[55]
			
    
    