import unittest
from calc_price import Calc_Price
import sys
import io

class CalcPriceTest(unittest.TestCase):
    def testCreate(self):
        outputtxt = io.StringIO()   
        iotext = io.StringIO("10")
        calc = Calc_Price(iotext,outputtxt)
        calc.calc_price()
        self.assertEqual(calc.outputtxt.getvalue(),"11\n")