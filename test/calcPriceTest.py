import unittest

from calcPrice import CalcPrice


class CalcPriceTest(unittest.TestCase):
    def testCreate(self):
        calc = CalcPrice()
        self.assertEqual(calc.calc_price([10, 12]), 24)
        self.assertEqual(calc.calc_price([40, 16]), 62)
        self.assertEqual(calc.calc_price([100, 45]), 160)
        self.assertEqual(calc.calc_price([50, 50, 55]), 171)
        self.assertEqual(calc.calc_price([]), 0)
