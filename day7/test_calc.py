import unittest
import calc


class TestCalc(unittest.TestCase):

    def test_add(self):
        result = calc.add(10, 5)
        self.assertEqual(result, 15)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_sub(self):
        self.assertEqual(calc.sub(0, -1), 1)
        self.assertEqual(calc.sub(10, 12), -2)

    def test_mul(self):
        self.assertEqual(calc.mul(0, 1), 0)
        self.assertEqual(calc.mul(10, -5), -50)
        self.assertEqual(calc.mul(-5, -5), 25)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 10), 1)

        with self.assertRaises(ValueError):
            calc.divide(10, 0)
        self.assertRaises(ValueError, calc.divide, 10, 0)


if __name__ == '__main__':
    unittest.main()
