import unittest
from main import largest_number_of_vehicles


class TestLargestNumberOfVehicles(unittest.TestCase):
    def test_case_1(self):
        input_data = [8, 4, 5, 4, 3, 1]
        expected_output = 3
        result = largest_number_of_vehicles(input_data)
        self.assertEqual(result, expected_output)

    def test_case_2(self):
        input_data = [60, 10, 11, 5, 13, 15, 7, 1, 18, 12, 16, 17]
        expected_output = 6
        result = largest_number_of_vehicles(input_data)
        self.assertEqual(result, expected_output)

    def test_case_3(self):
        input_data = [300, 25, 31, 19, 17, 4, 10, 37, 42, 35, 15, 43, 45, 30, 39, 9, 21, 33, 25, 3, 47, 41, 50, 18, 11,
                      26, 28]
        expected_output = 16
        result = largest_number_of_vehicles(input_data)
        self.assertEqual(result, expected_output)

    def test_case_4(self):
        input_data = [54, 10, 5, 6, 4, 7, 3, 8, 2, 9, 1, 10]
        expected_output = 9
        result = largest_number_of_vehicles(input_data)
        self.assertEqual(result, expected_output)

    def test_case_5(self):
        input_data = [2260, 50, 5, 24, 84, 58, 21, 57, 98, 51, 6, 16, 75, 95, 11, 23, 92, 85, 29, 56, 45, 55, 73, 20, 4,
                      34, 76, 96, 63, 30, 93, 2, 19, 39, 14, 71, 80, 40, 69, 54, 62, 42, 1, 10, 35, 8, 22, 70, 67, 15,
                      27, 38]
        expected_output = 50
        result = largest_number_of_vehicles(input_data)
        self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()
