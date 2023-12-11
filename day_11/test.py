import unittest

from solution import part_1, part_2, read_data


class TestSolution(unittest.TestCase):
    
    def test_part_1(self):
        sample_data = read_data("input_sample_part_1.txt")
        expected = 374

        actual = part_1(sample_data)

        self.assertEqual(expected, actual)

    def test_part_2(self):
        sample_data = read_data("input_sample_part_2.txt")
        expected_1 = 1030
        expected_2 = 8410
        
        actual_1 = part_2(sample_data, 10)
        actual_2 = part_2(sample_data, 100)

        self.assertEqual(expected_1, actual_1)
        self.assertEqual(expected_2, actual_2)

if __name__ == '__main__':
    unittest.main()
