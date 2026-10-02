import unittest
from Main import to_upper

class MyTestCase(unittest.TestCase):
    def test_to_upper(self):
        name = "Apurva"
        upper_name = to_upper(name)
        self.assertEqual(upper_name, "APURVA")

if __name__ == '__main__':
    unittest.main()