import unittest

from calcPrice import CalcPrice
import sys


class CalcPriceTest(unittest.TestCase):
    def testCreate(self):
        calc = CalcPrice()
        self.assertEqual(calc.calc_price([10, 12]), 24)
        self.assertEqual(calc.calc_price([40, 16]), 62)
        self.assertEqual(calc.calc_price([100, 45]), 160)
        self.assertEqual(calc.calc_price([50, 50, 55]), 171)
        self.assertEqual(calc.calc_price([]), 0)
        self.assertEqual(calc.calc_price([0, 0, 0, 0, 0]), 0)
        self.assertEqual(calc.calc_price([1000000]), 1100000)

        self.assertEqual(calc.calc_price([1000]), 1100)
        self.assertEqual(calc.calc_price([20, 40]), 66)
        self.assertEqual(calc.calc_price([30, 60, 90]), 198)
        self.assertEqual(calc.calc_price([11, 12, 13]), 40)

        print(calc.calc_price([10, 12]))
        print(calc.calc_price([40, 16]))
        print(calc.calc_price([100, 45]))
        print(calc.calc_price([50, 50, 55]))
        print(calc.calc_price([1000]))
        print(calc.calc_price([20, 40]))
        print(calc.calc_price([30, 60, 90]))
        print(calc.calc_price([11, 12, 13]))
