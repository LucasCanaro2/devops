import unittest
import calc


class testCalc(unittest.TestCase):
    def test_sum(self):
        result = calc.sum(3, 7)
        self.assertEqual(10, result)

    def test_sum2(self):
        self.assertEqual(0, calc.sum(-5.1, 5.10))

    def test_minus(self):
        self.assertEqual(5, calc.minus(10, 5))
