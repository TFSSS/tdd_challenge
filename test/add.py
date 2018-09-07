import unittest

from add import Add


class TestAdd(unittest.TestCase):
    def test_add(self):
        addCla = Add()
        # テスト対象インスタンス,,
        self.assertEqual(addCla.add(1, 2), 3)
        self.assertEqual(addCla.add(2, 2), 4)
