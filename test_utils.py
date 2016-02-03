# test_utils.py
# Author: Sébastien Combéfis
# Version: February 2, 2016

import unittest
import utils

class TestUtils(unittest.TestCase):
	def test_fact(self):
		self.assertEqual(1, utils.fact(0))
		self.assertEqual(1, utils.fact(1))
		self.assertEqual(6, utils.fact(3))
		with self.assertRaises(ValueError): utils.fact(-1)
	def test_roots(self):
		self.assertEqual((), utils.roots(0,0,5))
		self.assertEqual((1), utils.roots(0,1,-1))
		self.assertEqual((1,-1), utils.roots(1,0,-1))
	def test_integrate(self):
		self.assertEqual(-(4.0/3), utils.integrate('x ** 2 - 1',-1,1))
if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
	runner = unittest.TextTestRunner()
	exit(not runner.run(suite).wasSuccessful())