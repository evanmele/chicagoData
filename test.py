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
	
def createZipCodeToNeighborhoodDict:
	#returns dictionary to help user relate chicago neighborhoods with chicago zipcodes
	zip = dict()
	zip['hello'] = 'hola'
	zip['Rogers Park'] = '60626'
	zip['West Ridge'] = '60645'
	*zip['Uptown'] = '60640'
	*zip['Lincoln Square'] = '60625'
	*zip['North Center'] = '60613'
	*zip['Lake View'] = '60657'
	zip['Lincoln Park'] = '60614'
	zip['Near North Side'] ='60610'
	zip['Edison Park'] ='60631'
	zip['Norwood Park'] = '60631'
	*zip['Jefferson Park'] = '60630'
	*zip['Forest Glen'] = '60646'
	*zip['North Park'] = '60659'
	zip['Albany Park'] = '60625'
	zip['Portage Park'] = '60641'
	*zip['Irving Park'] = '60618'
zip['Dunning'] = '60635'
zip['Montclaire'] ='
zip['Belmont Cragin'] = '
zip['Hermosa'] ='
zip['Avondale'] = '
zip['Logan Square'] = '
zip['Humboldt park'] = '
zip['West Town'] = '
zip['Austin'] = '
zip['West Garfield Park'] = '
zip['East Garfield Park'] = '
zip['Near West Side'] = '
zip['North Lawndale'] =
zip['South Lawndale'] =
zip['Lower West Side'] =
zip['Loop'] =
zip['Near South Side'] =
zip['Armour Square'] = 
zip['Douglas'] =
zip['Oakland'] =
zip['Fuller Park'] =
zip['Grand Boulevard'] =
zip['Kenwood'] =
zip['Washington Park'] =
zip['Hyde Park'] =
zip['Woodlawn'] =
zip['South Shore'] =
zip['Chatham'] =
zip['Avalon Park'] =
zip['South Chicago'] =
zip['Burnside'] =
zip['Calumet Heights'] =
zip['Roseland'] =
zip['Pullman'] =
zip['South Deering'] =
zip['East Side'] =
zip['West Pullman'] =
zip['Riverdale'] =
zip['Hegewisch'] =
zip['Garfield Ridge'] =
zip['Archer Heights'] =
zip['Brighton Park'] =
zip['McKinley Park'] =
zip['Bridgeport'] =
zip['New City'] =
zip['West Elsdon] =
zip['Gage Park'] =
zip['Clearing']
zip['West Lawn'] =
zip['Chicago Lawn'] =
zip['West Englewood'] =
zip['Englewood'] = 
zip['Greater Grand Crossing'] =
zip['Ashburn'] =
zip['Auburn Gresham']
zip['Beverly'] = 
zip['Washington Heights'] =
zip['Mount Greenwood'] =
zip['Morgan Park'] =
zip["O'Hare"] =
zip['Edgewater'] =