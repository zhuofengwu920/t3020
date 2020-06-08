
import unittest

import io

from unittest.mock import patch

import sys

class TestDatamunger(unittest.TestCase):

    def test_calc_total(self):

        args = [None, "data.csv"]

        with patch('sys.argv', args):
            import code

            test_curr = [44,2,3,4,5,6,7,8,9,0]
            result = code.calc_total(test_curr)

            self.assertEqual(result, test_curr[0])

            test_curr = [32,2,3,4,5,4,7,8,9,10]
            result = code.calc_total(test_curr)

            self.assertNotEqual(result, test_curr[0])


    def test_check_monotonic(self):

        args = [None, "data.csv"]

        with patch('sys.argv', args):
            import code

            n = 58

            test_prev = [35,2,3,4,5,6,7,8,9,10]
            test_curr = [147,2,6,4,89,6,23,8,9,10]

            cap = io.StringIO()
            sys.stdout = cap

            code.check_monotonic(n, test_prev, test_curr)

            sys.stdout = sys.__stdout__

            result = cap.getvalue()

            self.assertEqual(result, "")

            n = 12

            test_prev = [35,4,3,4,5,6,7,8,9,10]
            test_curr = [147,2,6,4,89,6,23,8,9,10]

            cap = io.StringIO()
            sys.stdout = cap

            code.check_monotonic(n, test_prev, test_curr)

            sys.stdout = sys.__stdout__

            result = cap.getvalue()

            self.assertEqual(result, "Monotonic error at column 1 comparing lines 11 and 12   values 2 and 4\n")

    def test_check_row(self):

        args = [None, "data.csv"]

        with patch('sys.argv', args):
            import code

            n = 50

            test_prev = [35,2,3,4,5,6,7,8,9,10]
            test_curr = [68,3,6,4,9,6,23,8,9,10]

            result = code.check_row(n, test_prev, test_curr)

            self.assertTrue(result)

            n = 50

            test_prev = [35,2,3,4,5,6,7,8,9,10]
            test_curr = [68,'',6,4,9,6,23,8,9,10]

            result = code.check_row(n, test_prev, test_curr)

            self.assertFalse(result)




if __name__ == '__main__':

    unittest.main()