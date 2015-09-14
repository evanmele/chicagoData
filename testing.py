import unittest
import data
import csv

class DataTests(unittest.TestCase):
	def test_five_plus_five(self):
		assert 5 + 5 == 10
	
	def test_one_plus_one(self):
		assert not  1 + 1 == 3
	
	#test to see if disease list made was made in the correct order
	def test_disease_count(self):
		diseases = data.diseaseCount()
		self.assertEquals(diseases[0], 9260.6)	
		self.assertEquals(diseases[1], 8479.7)
		self.assertEquals(diseases[2], 8318.6)
		self.assertEquals(diseases[3], 7844.7)
		self.assertEquals(diseases[4], 7765.5) 
	
	#testing proper setup of dictionary that will translate between neighborhood and zipcode
	def test_neighborhoodToZip(self):
		dict = data.createZipCodeToNeighborhoodDict()
		self.assertEquals(dict['Rogers Park'], '60626')
		self.assertEquals(dict['Edgewater'], '60660')
		self.assertEquals(dict['West Ridge'], '60645')
		
	#testing transmission to neighborhood relationship
	def test_transmissionToNeighborhoodDict(self):
		dict = data.createTransmissionDict()
		self.assertEquals(dict[9260.6], 'West Garfield Park')
		self.assertEquals(dict[8479.7], 'North Lawndale')
		self.assertEquals(dict[8318.6], 'Fuller Park')
		self.assertEquals(dict[7844.7], 'East Garfield Park')
		self.assertEquals(dict[7765.5], 'West Englewood')
	
	#test to see if full range of zipcode influence made it into the list
	def test_zipcounts(self):
		lst = data.zipCodeMax()
		self.assertEquals(lst[0], 11)
		self.assertEquals(lst[len(lst)-1], 1)
	
	
	
	if __name__ == '__main__':
		unittest.main()