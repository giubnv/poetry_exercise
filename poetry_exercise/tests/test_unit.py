import unittest
from poetry_exercise.src.main import ApproxMath, ExactMath
import math


class MyTestCase(unittest.TestCase):
    def test_mymath_approx(self):

        x = 100
        expected_x = 10.0
        expected_x_2 = 10.005721542003908

        y = math.pi / 3
        expected_y = 1.0233267079464885
        expected_y_2 = 1.0471975511965976

        test_ma = ApproxMath()
        test_me = ExactMath()

        self.assertEqual(expected_x, test_me.sqrt(x))
        self.assertEqual(expected_x_2,test_ma.sqrt(x))

        self.assertEqual(expected_y, test_me.sqrt(y))
        self.assertEqual(expected_y_2, test_ma.sqrt(y))



if __name__ == '__main__':
    unittest.main()
