import unittest
from calc_price import Calc_Price
import sys
import io

class CalcPriceTest(unittest.TestCase):
    def testCreate(self):
        iotext = io.StringIO("10")
        sys.stdout = iotext
        calc = Calc_Price(iotext)
        self.assertEqual(iotext.getvalue(),"11")