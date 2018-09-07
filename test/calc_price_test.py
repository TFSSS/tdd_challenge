import unittest
from calc_price import Calc_Price
import sys
import io

class CalcPriceTest(unittest.TestCase):
    def testCreate(self):


        self.lineText("""10,12
40,16
100,45

50,50,55""","""24
62
160
0
171
""")

    def lineText(self,txt,expecttxt):
        outputtxt = io.StringIO()
        iotext = io.StringIO(txt)
        calc = Calc_Price(iotext, outputtxt)
        calc.calc_price()
        self.assertEqual(calc.outputtxt.getvalue(), expecttxt)