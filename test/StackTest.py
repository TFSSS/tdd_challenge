import unittest

from stack import Stack


class StackTest(unittest.TestCase):
    def testCreate(self):
        stack = Stack()
        self.assertEqual(stack.isEmpty(), True)
