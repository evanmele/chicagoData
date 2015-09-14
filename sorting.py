import csv
#adddddd this!
#this program finds the 5 highest amount of cases of chlamydia per neighborhood"

f = open("disease1.csv")

csv_f = csv.reader(f) #csv reader object/list

diseases = []

#skip over first row to avoid parsing errors, headers not needed really
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



#################################################################


#create dictionary of each transmission rate associated with each neighborhood.
#the transmission rate will serve as the key in the hash map, and the neighbohoor will be the value






#diseases.sort()
#print diseases
