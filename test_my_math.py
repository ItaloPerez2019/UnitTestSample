import mymath
import unittest

# create unit test cases to test all the above functions. [ dont use python built in min function, write your own
# python script to test the list]


class Test_myMath(unittest.TestCase):
    def test_max_integers(self):

        result = mymath.max_num([232, 23, 1, 2, 1])
        self.assertEqual(result, 232)

    def test_min_integers(self):

        result = mymath.min_num([232, 23, 2, 2, 2])
        self.assertTrue(result, 1)

    def test_avg_integers(self):

        result = mymath.avg_num([1, 312, 1])
        self.assertTrue(result, 2.3333)


if __name__ == '__main__':
    unittest.main()