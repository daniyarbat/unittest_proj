import unittest
from utils import arrs

class TestArrs(unittest.TestCase):

    def test_get_existing_index(self):
        self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 2)

    def test_get_non_existing_index_with_default(self):
        self.assertEqual(arrs.get([1, 2, 3], 10, "test"), "test")

    def test_get_negative_index_with_default(self):
        self.assertEqual(arrs.get([1, 2, 3], -1, "test"), "test")

    def test_get_empty_list(self):
        self.assertEqual(arrs.get([], 0, "test"), "test")

    def test_get_negative_index(self):
        self.assertIsNone(arrs.get([1, 2, 3], -1))

    def test_get_index_beyond_length(self):
        self.assertIsNone(arrs.get([1, 2, 3], 3))

    def test_my_slice_default(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_my_slice_with_start(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4, 5], 2), [3, 4, 5])

    def test_my_slice_with_end(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4, 5], None, 3), [1, 2, 3])

    def test_my_slice_with_negative_start(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4, 5], -2), [4, 5])

    def test_my_slice_with_negative_end(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4, 5], None, -2), [1, 2, 3])

    def test_my_slice_with_negative_start_and_end(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4, 5], -3, -1), [3, 4])

    def test_my_slice_empty_list(self):
        self.assertEqual(arrs.my_slice([], 1, 3), [])

if __name__ == '__main__':
    unittest.main()


