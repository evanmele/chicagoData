import csv


##########print zipCountsDict
#print frequency chart, for zipcode x, the amount of condom distribution sites are x, y, z
#these neighborhoods correlate with neighborhoods x, y, and z

#the neighborhoods with the highest reported chlamydia rates are x, y and z
#the neighborhoods with the highest reported teen birth rates are x, y and z




#notes: find top 5 diseased neighborhoods by putting into list and sorting, then put those
#neighborhoods into the dictionaries to find the most highly diseased area, then cross check that with
#best covered areas for condom sites.

#returns a dictionary that counts the number of condom distribution sites that are available in each the zipcode	
def zipCodeInfluence():
	#load .csv that shows which zipcodes had available condom distribution sites
	f = open("condoms.csv")
	csv_f = csv.reader(f) #csv reader object/list
	#create list to hold zipcodes
	zipcodes = []
	#loop over every row and pull the zipcode from the dataset, compile into one list.
	for row in csv_f:
		#add each zipcode to list
		zipcodes.append(row[5])
	f.close()
	#create dictionary to relate the zipcodes and their amount of distribution sites
	zipCountsDict = dict()
	#load concentrations into each zipcode in the dictionary
	for zip in zipcodes:
		zipCountsDict[zip] = zipcodes.count(zip)
	return zipCountsDict
	

#returns a dictionary of the zipcodes of condom sites linked to the # of sites in the zipcode

def clinicCount():
	#returns a list of zipcodes that have clinics available.
	clinics = open("clinics.csv")
	csv_clinics = csv.reader(clinics) #csv reader object
	clinicZipcodes = []
	
	for row in csv_clinics:
		clinicZipcodes.append(row[5])
		#print row[5]
	clinics.close()
	return clinicZipcodes
	

#returns the top 5 disease infection rates in 2013
def diseaseCount():
	f = open("disease1.csv")
	csv_f = csv.reader(f) #csv reader object/list
	diseases = []  #list to hold the disease figures per neighborhood
	#skip over first row to avoid parsing errors, headers not needed really
	csv_f.next()
	#loop over every row and pull the zipcode from the dataset, compile into one list.
	for row in csv_f:
		#print all lines in csv ..... print row
		if row[55] != "":
			#convert csv data into float so it may be sorted appropriately
			infectionAmount = float(row[55])
			#add the float to the list
			diseases.append(infectionAmount)
			print row[55] + '\n'
	f.close() ##close file
	#sort diseases from lowest to highest
	diseases.sort()
	#reverse to get highest to lowest
	diseases.reverse()
	#print the top 5
	print "The most cases reported in 2013 by neighbhorhood were " + "\n" 
	print diseases[0]
	print diseases[1]
	print diseases[2]
	print diseases[3]
	print diseases[4]
	
	return diseases #returns list of diseases sorted highest to lowest



	
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
			infectionAmount = float(row[55])
			transmissions[infectionAmount] = row[1]
		
	return transmissions


	
	
def createZipCodeToNeighborhoodDict():
	#returns dictionary to help user relate chicago neighborhoods with chicago zipcodes
	zip = dict()
	zip['hello'] = 'hola'
	zip['Rogers Park'] = '60626'
	zip['West Ridge'] = '60645'
	zip['Uptown'] = '60640'
	zip['Lincoln Square'] = '60625'
	zip['North Center'] = '60613'
	zip['Lake View'] = '60657'
	zip['Lincoln Park'] = '60614'
	zip['Near North Side'] ='60610'
	zip['Edison Park'] ='60631'
	zip['Norwood Park'] = '60631'
	zip['Jefferson Park'] = '60630'
	zip['Forest Glen'] = '60646'
	zip['North Park'] = '60659'
	zip['Albany Park'] = '60625'
	zip['Portage Park'] = '60641'
	zip['Irving Park'] = '60618'
	zip['Dunning'] = '60635'
	zip['Montclaire'] ='60634'
	zip['Belmont Cragin'] = '60641'
	zip['Hermosa'] ='60639'
	zip['Avondale'] = '60618'
	zip['Logan Square'] = '60622'
	zip['Humboldt park'] = '60651'
	zip['West Town'] = '60612'
	zip['Austin'] = '60651'
	zip['West Garfield Park'] = '60624'
	zip['East Garfield Park'] = '60624'
	zip['Near West Side'] = '60661'
	zip['North Lawndale'] = '60623'
	zip['South Lawndale'] = '60623'
	zip['Lower West Side'] = '60616'
	zip['Loop'] = '60604'
	zip['Near South Side'] = '60607'
	zip['Armour Square'] = '60609'
	zip['Douglas'] = '60609'
	zip['Oakland'] = '60653'
	zip['Fuller Park'] = '60609'
	zip['Grand Boulevard'] = '60615'
	zip['Kenwood'] = '60615'
	zip['Washington Park'] = '60621'
	zip['Hyde Park'] = '60637'
	zip['Woodlawn'] = '60637'
	zip['South Shore'] = '60619'
	zip['Chatham'] = '60620'
	zip['Avalon Park'] = '60617'
	zip['South Chicago'] = '60617'
	zip['Burnside'] = '60619'
	zip['Calumet Heights'] = '60619'
	zip['Roseland'] = '60620'
	zip['Pullman'] = '60628'
	zip['South Deering'] = '60633'
	zip['East Side'] = '60617'
	zip['West Pullman'] = '60643'
	zip['Riverdale'] = '60627'
	zip['Hegewisch'] = '60633'
	zip['Garfield Ridge'] = '60638'
	zip['Archer Heights'] = '60632'
	zip['Brighton Park'] = ' 60632'
	zip['McKinley Park'] = '60609'
	zip['Bridgeport'] = '60616'
	zip['New City'] = '60609'
	zip['West Elsdon'] = '60629'
	zip['Gage Park'] = '60636'
	zip['Clearing'] = '60638'
	zip['West Lawn'] = '60629'
	zip['Chicago Lawn'] = '60636'
	zip['West Englewood'] = '60636'
	zip['Englewood'] = '60621'
	zip['Greater Grand Crossing'] = '60637'
	zip['Ashburn'] = '60652'
	zip['Auburn Gresham'] = '60620'
	zip['Beverly'] = '60643'
	zip['Washington Heights'] = '60628'
	zip['Mount Greenwood'] = '60655'
	zip['Morgan Park'] = '60643'
	zip["O'Hare"] = '60666'
	zip['Edgewater'] = '60660'
	return zip
	

def main():
	#load dictionary that relates zipcodes with neighborhoods -> will for sure use this later
	zipToNeighborhood = createZipCodeToNeighborhoodDict()
	#print zipToNeighborhood
	zipCodeCount = zipCodeInfluence()
	
	print "The zipcodes and the amount of condom distribution sites are as follows:" + "\n"
	print zipCodeCount
	#zipcodes with the most sites are....?
	
	print "The zipcodes that have STI clinics available are " "\n"
	clinics = clinicCount()
	print clinics
	
	
	#load dictionary of 
	transmissionsToNeighborhoods = createTransmissionDict()
	#load list of transmissions
	transmissionCount = diseaseCount()
	print transmissionCount
	
	#display the most infected neighborhoods and their respective zip codes.
	print "the top 5 most infected neighborhoods are..." + "\n"
	hood1 = transmissionsToNeighborhoods[transmissionCount[0]]
	hood2 = transmissionsToNeighborhoods[transmissionCount[1]]
	hood3 = transmissionsToNeighborhoods[transmissionCount[2]]
	hood4 = transmissionsToNeighborhoods[transmissionCount[3]]
	hood5 = transmissionsToNeighborhoods[transmissionCount[4]]
	print hood1 + ", " + hood2 + ", " + hood3 + ", " + hood4 + ", " + hood5
	zip1 = zipToNeighborhood[hood1]
	zip2 = zipToNeighborhood[hood2]
	zip3 = zipToNeighborhood[hood3]
	zip4 = zipToNeighborhood[hood4]
	zip5 = zipToNeighborhood[hood5]
	print " \nthe zipcodes of these neighborhoods are: " + zip1 + ", " + zip2 + ", " + zip3 + ", " + zip4 + ", " + zip5 + "\n"
	
	#check to see how many condom distribution sites are available in these zipcodes!
	print "the amount of condom distribution sites present in these neighborhoods are as follows..."
	print zipCodeCount[zip1], zipCodeCount[zip2], zipCodeCount[zip3], zipCodeCount[zip4], zipCodeCount[zip5]
	
	
	
	
		
	
	
	

main()
	
