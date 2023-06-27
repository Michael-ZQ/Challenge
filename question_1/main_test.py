import unittest
from question_1.main import truncated_float_sum


class TruncatedFloatSumTestCase(unittest.TestCase):

    def test_valid_input(self):
        a = 3.14159
        b = 2.71828
        result = truncated_float_sum(a, b)
        self.assertEqual(result, 5)

    def test_invalid_input_a(self):
        a = 0.05
        b = 10000000
        result = truncated_float_sum(a, b)
        self.assertEqual(result, "Invalid input")


if __name__ == '__main__':
    unittest.main()
