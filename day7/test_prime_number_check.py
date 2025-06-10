from day2 import prime_numeber_check
import unittest
import sys

sys.path.append("C:\\Users\\Administrator\\Desktop\\valere labs")


class TestPrimeCheck(unittest.TestCase):

    def test_primenumcheck(self):
        self.assertEqual(prime_numeber_check.primenum(11), True)
        self.assertEqual(prime_numeber_check.primenum(2), True)
        self.assertEqual(prime_numeber_check.primenum(1), False)
        self.assertEqual(prime_numeber_check.primenum(997), True)
        self.assertEqual(prime_numeber_check.primenum(-1), False)
        self.assertEqual(prime_numeber_check.primenum(0), False)


if __name__ == '__main__':
    unittest.main()
