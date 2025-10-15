# test_module.py
import unittest
import mean_var_std

class UnitTests(unittest.TestCase):
    def test_calculate_function(self):
        # Test with the example list
        expected = {
          'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
          'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667],
          'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611],
          'max': [[6, 7, 8], [2, 5, 8], 8],
          'min': [[0, 1, 2], [0, 3, 6], 0],
          'sum': [[9, 12, 15], [3, 12, 21], 36]
        }
        actual = mean_var_std.calculate([0,1,2,3,4,5,6,7,8])
        self.assertAlmostEqual(actual['mean'][2], expected['mean'][2])
        self.assertAlmostEqual(actual['variance'][2], expected['variance'][2])
        self.assertAlmostEqual(actual['standard deviation'][2], expected['standard deviation'][2])
        self.assertEqual(actual['max'][2], expected['max'][2])
        self.assertEqual(actual['min'][2], expected['min'][2])
        self.assertEqual(actual['sum'][2], expected['sum'][2])


    def test_value_error_exception(self):
        # Test if the function raises a ValueError for lists with less than 9 numbers
        with self.assertRaises(ValueError):
            mean_var_std.calculate([1, 2, 3, 4, 5, 6, 7])

if __name__ == "__main__":
    unittest.main()