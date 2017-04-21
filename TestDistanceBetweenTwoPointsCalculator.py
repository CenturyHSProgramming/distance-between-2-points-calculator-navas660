# TestDistanceBetweenPointsCalculator.py

###################################
#   What are we testing for?
#     Wide range of inputs
#     Correct outputs
###################################

# Import Statements
import unittest
import DistanceBetweenPointsCalculator

class KnownValues(unittest.TestCase):
    # Formula for unittest method is:
    # test_functionName_testDescription

    def test_calculateDistanceBetween_for6_8_0_0(self):
        # Capture the results of the function
        result = DistanceBetweenPointsCalculator.calculateDistanceBetween(6, 8, 0, 0)
        # Check for expected output
        self.assertEqual(10.0, result)

    def test_calculateDistanceBetween_for_2_4_26_9(self):
        result = DistanceBetweenPointsCalculator.calculateDistanceBetween(2, 4, 26, 9)
        expected = 24.52
        self.assertEqual(expected, result)

    # Add minimum of 5 more unittests
    def test_calculateDistanceBetween_for_4_6_28_13(self):
        result = DistanceBetweenPointsCalculator.calculateDistanceBetween(4, 6, 28, 13)
        expected = 25.0
        self.assertEqual(expected, result)

    def test_calculateDistanceBetween_for_24_1_13_30(self):
        result = DistanceBetweenPointsCalculator.calculateDistanceBetween(24, 1, 13, 30)
        expected = 31.02
        self.assertEqual(expected, result)

    def test_calculateDistanceBetween_for_neg10_1_neg20_10(self):
        result = DistanceBetweenPointsCalculator.calculateDistanceBetween(-1,0, 1, -20, 10)
        expected = 13.45
        self.assertEqual(expected, result)

    def test_calculateDistanceBetween_for_neg6_neg2_20_10(self):
        result = DistanceBetweenPointsCalculator.calculateDistanceBetween(-6, -2, 20, 10)
        expected = 28.64
        self.assertEqual(expected, result)

    def test_calculateDistanceBetween_for_60_20_neg20_neg10(self):
        result = DistanceBetweenPointsCalculator.calculateDistanceBetween(60, 20, -20, -10)
        expected = 85.44
        self.assertEqual(expected, result)

    def test_calculateDistanceBetween_for_10_5_6_2(self):
        result = DistanceBetweenPointsCalculator.calculateDistanceBetween(10, 5, 6, 2)
        expected = 5.0
        self.assertEqual(expected, result)


# Run the tests
if __name__ == '__main__':
    unittest.main()
