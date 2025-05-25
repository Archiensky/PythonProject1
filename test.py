import unittest
from less8 import *

class My_Test(unittest.TestCase):
    def test_args(self):
        self.assertEqual(adder(7, 2), 9)
