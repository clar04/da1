import unittest
import mean_var_std

class UnitTests(unittest.TestCase):
    def assertAlmostEqualList(self, list1, list2, places=7):
        """Helper function to compare lists with floating point tolerance"""
        self.assertEqual(len(list1), len(list2))
        for i in range(len(list1)):
            if isinstance(list1[i], list):
                self.assertAlmostEqualList(list1[i], list2[i], places)
            else:
                self.assertAlmostEqual(list1[i], list2[i], places=places)
    
    def assertAlmostEqualDict(self, dict1, dict2, places=7):
        """Helper function to compare dictionaries with floating point tolerance"""
        self.assertEqual(set(dict1.keys()), set(dict2.keys()))
        for key in dict1.keys():
            if isinstance(dict1[key], list):
                self.assertAlmostEqualList(dict1[key], dict2[key], places)
            else:
                self.assertAlmostEqual(dict1[key], dict2[key], places=places)
    def test_calculate(self):
        actual = mean_var_std.calculate([0,1,2,3,4,5,6,7,8])
        expected = {
            'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
            'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667],
            'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611],
            'max': [[6, 7, 8], [2, 5, 8], 8],
            'min': [[0, 1, 2], [0, 3, 6], 0],
            'sum': [[9, 12, 15], [3, 12, 21], 36]
        }
        self.assertAlmostEqualDict(actual, expected, places=6)

    def test_calculate2(self):
        actual = mean_var_std.calculate([9,1,5,3,3,3,2,9,0])
        expected = {
            'mean': [[4.666666666666667, 4.333333333333333, 2.6666666666666665], [5.0, 3.0, 3.6666666666666665], 3.888888888888889],
            'variance': [[9.555555555555557, 11.555555555555557, 4.222222222222222], [10.666666666666666, 0.0, 14.888888888888891], 9.209876543209875],
            'standard deviation': [[3.0912061651652345, 3.39934634239519, 2.0548046676563256], [3.265986323710904, 0.0, 3.8586123009300755], 3.0347778408328137],
            'max': [[9, 9, 5], [9, 3, 9], 9],
            'min': [[2, 1, 0], [1, 3, 0], 0],
            'sum': [[14, 13, 8], [15, 9, 11], 35]
        }
        self.assertAlmostEqualDict(actual, expected, places=6)
    
    def test_calculate_with_few_digits(self):
        with self.assertRaises(ValueError, msg="Expected ValueError when calling 'calculate()' with a list with less than 9 numbers."):
            mean_var_std.calculate([2,6,2,8,4,0,1,])

if __name__ == "__main__":
    unittest.main()