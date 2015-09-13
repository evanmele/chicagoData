import csv

print "this program counts the amount of cases of chlamydia"

f = open("disease1.csv")

csv_f = csv.reader(f) #csv reader object/list

diseases = []
#zipcodes.append(row[5])
#print zipcodes
#print len(zipcodes)
#zipcodes1 = set(zipcodes1)
#zipcodes2 = set(zipcodes2)
#print zipcodes2.intersection(zipcodes1)


#skip over first rrow
csv_f.next()

#loop over every row and pull the zipcode from the dataset, compile into one list.
for row in csv_f:
	#print all lines in csv ..... print row
	if row[55] != "":
		infectionAmount = float(row[55])
		diseases.append(infectionAmount)
		print row[55] + '\n'
f.close()

##for disease in diseases[1:]
#	float(disease)


diseases.sort()
print diseases
diseases.reverse()
print "The most cases reported in 2013 by neighbhorhood were " + "\n" 
print diseases[0]
print diseases[1]
print diseases[2]
print diseases[3]
print diseases[4]


#create 




#diseases.sort()
#print diseases
