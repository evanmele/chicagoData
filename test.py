import csv

f = open("condoms.csv")

csv_f = csv.reader(f) #csv reader object/list

zipcodes = []
#zipcodes.append(row[5])
#print zipcodes
#print len(zipcodes)
#zipcodes1 = set(zipcodes1)
#zipcodes2 = set(zipcodes2)
#print zipcodes2.intersection(zipcodes1)

#loop over every row and pull the zipcode from the dataset, compile into one list.
for row in csv_f:
	#print all lines in csv ..... print row
	zipcodes.append(row[5])
	#print row[5]
f.close()
#print zipcodes
zipCount = zipcodes.count('60612')
print zipCount


zipCountsDict = dict()


for zip in zipcodes:
	zipCountsDict[zip] = zipcodes.count(zip)
	#print zip , zipcodes.count(zip);
	
print zipCountsDict
#print frequency chart, for zipcode x, the amount of condom distribution sites are x, y, z
#these neighborhoods correlate with neighborhoods x, y, and z

#the neighborhoods with the highest reported chlamydia rates are x, y and z
#the neighborhoods with the highest reported teen birth rates are x, y and z


#returns a dictionary of the zipcodes of condom sites linked to the # of sites in the zipcode

def zipCodeInfluence:
	zipCountsDict = dict()
	for zip in zipcodes:
		zipCounts Dict[zip] = zipcodes.count(zip)
	return zipCountsDict