import unittest
from calculator import Calculator

class Test(unittest.TestCase):
    def test_add(self):
        c = Calculator()
        c.btnclear_pressed()
        c.btn2_pressed()
        c.btnplus_pressed()
        c.btn2_pressed()
        c.btn2_pressed()
        self.assertEqual(c.btnequal_pressed(), "24")
        
    def test_minus(self):
        c = Calculator() 
        c.btnclear_pressed()
        c.btn2_pressed()
        c.btnminus_pressed()
        c.btn2_pressed()
        c.btn2_pressed()
        self.assertEqual(c.btnequal_pressed(), "-20")

    def test_multiply(self):
        c = Calculator() 
        c.btnclear_pressed()
        c.btn2_pressed()
        c.btnmultiply_pressed()
        c.btn2_pressed()
        self.assertEqual(c.btnequal_pressed(), "4")
    
    def test_divide(self):
        c = Calculator() 
        c.btnclear_pressed()
        c.btn2_pressed()
        c.btndivide_pressed()
        c.btn2_pressed()
        self.assertEqual(c.btnequal_pressed(), "1.0")
    
    def test_multiple_operations(self):
        c = Calculator()
        c.btnclear_pressed() 
        c.btn9_pressed()
        c.btn9_pressed()
        c.btnminus_pressed()
        c.btn3_pressed()
        c.btn6_pressed()
        c.btndivide_pressed()
        c.btn9_pressed()
        c.btnplus_pressed()
        c.btn3_pressed()
        c.btnmultiply_pressed()
        c.btn6_pressed()
        self.assertEqual(c.btnequal_pressed(), "113.0")


if __name__ == "__main__":
    unittest.main()
