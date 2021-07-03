import unittest
from calculator import Calculator

class Test(unittest.TestCase):
    def test_add(self):
        c = Calculator() 
        c.btn2_pressed()
        c.btnplus_pressed()
        c.btn2_pressed()
        c.btn2_pressed()
        self.assertEqual(c.btnequal_pressed(), "24")


if __name__ == "__main__":
    unittest.main()