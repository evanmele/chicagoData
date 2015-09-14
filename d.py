import csv

print "this program generates a hashmap that relates transmission rate in 2013 to the neighborhood it was found in"



#returns dictionary that holds the hashmap between transmission rates and the neighborhood they belong to
def createTransmissionDict():
	#create dictionary
	transmissions = dict()
	f = open("disease1.csv")  #make the filename a parameter later.
	csv_f = csv.reader(f) #csv reader object/list
	#skip first line due to titles
	csv_f.next()
	for row in csv_f:
		if row[55] != "":
		#convert to float so that it can interact with other functions appropriately.
			infectionAmount = float(row[55])
			transmissions[infectionAmount] = row[1]
		
	return transmissions
	

#createTransmissionDict()
trans = createTransmissionDict();
print trans
