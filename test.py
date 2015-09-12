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

def zipCodeInfluence():
	zipCountsDict = dict()
	for zip in zipcodes:
		zipCountsDict[zip] = zipcodes.count(zip)
	return zipCountsDict
	
	

#could create a set of zipcodes based on the condom data, then use those as the key, but might be too complex...
	
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