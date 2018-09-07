import unittest

from stack import Stack
from calcPrice import CalcPrice


class StackTest(unittest.TestCase):
    def testCreate(self):
        # stack = Stack()
        # self.assertEqual(stack.isEmpty(), True)
        calc = CalcPrice()
        self.assertEqual(calc.calc_price([10, 12]), 24)
