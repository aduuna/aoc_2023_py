import unittest

from solution import part_1, part_2, read_data


class TestSolution(unittest.TestCase):
    
    def test_part_1(self):
        sample_data = read_data("input_sample_part_1.txt")
        expected = 4

        actual = part_1(sample_data)

        self.assertEqual(expected, actual)

        sample_data = read_data("input_sample_part_1.2.txt")
        expected = 8

        actual = part_1(sample_data)

        self.assertEqual(expected, actual)

    def test_part_2(self):
        sample_data = read_data("input_sample_part_2.txt")
        expected = 4
        
        actual = part_2(sample_data)

        self.assertEqual(expected, actual)

        sample_data = read_data("input_sample_part_2.2.txt")
        expected = 4
        
        actual = part_2(sample_data)

        self.assertEqual(expected, actual)

        sample_data = read_data("input_sample_part_2.3.txt")
        expected = 8
        
        actual = part_2(sample_data)

        self.assertEqual(expected, actual)

        sample_data = read_data("input_sample_part_2.4.txt")
        expected = 10
        
        actual = part_2(sample_data)

        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
