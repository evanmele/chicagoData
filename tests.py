import unittest
import data

class DataTests(unittest.TestCase):
	def test_five_plus_five(self):
		assert 5 + 5 == 10
	
	def test_one_plus_one(self):
		assert not 1 + 1 == 3