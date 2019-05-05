import unittest
from numberAddCommas import addCommas 

class addCommasUnitTest(unittest.TestCase):    
    def setUp(self):
      pass

    def tearDown(self):
      pass

    def test_Positive_Number(self):
        ipunt = 12345678
        expected_result = "12,345,678"
        result = addCommas(ipunt)
        self.assertEqual(expected_result,result)

    def test_Negative_Number(self):
        ipunt = -6489752
        expected_result = "-6,489,752"
        result = addCommas(ipunt)
        self.assertEqual(expected_result,result)

    def test_Decimal_Number(self):
        ipunt = 48846.1546
        expected_result = "48,846.1546"
        result = addCommas(ipunt)
        self.assertEqual(expected_result,result)

if __name__ == '__main__':
    unittest.main()
