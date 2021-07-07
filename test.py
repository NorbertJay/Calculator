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
        
    def test_dot_del_par(self):
        c = Calculator()
        c.btnclear_pressed() 
        c.btnbl_pressed()
        c.btn9_pressed()
        c.btn9_pressed()
        c.btnminus_pressed()
        c.btn3_pressed()
        c.btn6_pressed()
        c.btnbr_pressed()
        c.btndivide_pressed()
        c.btn9_pressed()
        c.btnplus_pressed()
        c.btn3_pressed()
        c.btnmultiply_pressed()
        c.btn6_pressed()
        c.btnmultiply_pressed()
        c.btn1_pressed()
        c.btn0_pressed()
        c.btndelete_pressed()
        self.assertEqual(c.btnequal_pressed(), "25.0")
    
    def test_power(self):
        c = Calculator() 
        c.btnclear_pressed()
        c.btn9_pressed()
        c.btnpower_pressed()
        c.btn1_pressed()
        self.assertEqual(c.btnequal_pressed(), "9")

    def test_sin(self):
        c = Calculator() 
        c.btnclear_pressed()
        c.btn0_pressed()
        c.btnsin_pressed()
        self.assertEqual(c.btnequal_pressed(), "0.0")
    
    def test_sin2(self):
        c = Calculator() 
        c.btnclear_pressed()
        c.btn6_pressed()
        c.btn9_pressed()
        c.btnsin_pressed()
        self.assertEqual(c.btnequal_pressed(), "-0.11478481378318722")
    
    def test_cos(self):
        c = Calculator() 
        c.btnclear_pressed()
        c.btn0_pressed()
        c.btncos_pressed()
        self.assertEqual(c.btnequal_pressed(), "1.0") 
    
    def test_cos2(self):
        c = Calculator() 
        c.btnclear_pressed()
        c.btn4_pressed()
        c.btn5_pressed()
        c.btncos_pressed()
        self.assertEqual(c.btnequal_pressed(), "0.5253219888177297") 
        
    
    def test_tan(self):
        c = Calculator() 
        c.btnclear_pressed()
        c.btn0_pressed()
        c.btntan_pressed()
        self.assertEqual(c.btnequal_pressed(), "0.0") 

    def test_tan2(self):
        c = Calculator() 
        c.btnclear_pressed()
        c.btn5_pressed()
        c.btntan_pressed()
        self.assertEqual(c.btnequal_pressed(), "-3.380515006246586") 
        
    def test_round(self):
        c = Calculator() 
        c.btnclear_pressed()
        c.btn6_pressed()
        c.btn6_pressed()
        c.btndot_pressed()
        c.btn1_pressed()
        self.assertEqual(c.btnround_pressed(), "66") 
    
    def test_logarithm(self):
        c = Calculator() 
        c.btnclear_pressed()
        c.btn1_pressed()
        c.btn0_pressed()
        c.btn0_pressed()
        c.btnlog_pressed()
        self.assertEqual(c.btnround_pressed(), "2")
    
    def test_par(self):
        c = Calculator
        c.btnclear_pressed(c)
        c.btn1_pressed(c)
        c.btnplus_pressed(c)
        c.btnbl_pressed(c)
        c.btn3_pressed(c)
        c.btnminus_pressed(c)
        c.btn2_pressed(c)
        c.btnmultiply_pressed(c)
        c.btn4_pressed(c)
        c.btnbr_pressed(c)
        self.assertEqual(c.btnequal_pressed(c), "-4")
    
    def test_ln(self):
        c = Calculator
        c.btnclear_pressed(c)
        c.btn5_pressed(c)
        c.btnln_pressed(c)
        self.assertEqual(c.btnequal_pressed(c), "1.6094379124341003")
        
    def test_factorial(self):
        c = Calculator() 
        c.btnclear_pressed()
        c.btn1_pressed()
        c.btn3_pressed()
        c.btnfact_pressed()
        self.assertEqual(c.btnequal_pressed(), "6227020800")

    def test_square_root(self):
        c = Calculator() 
        c.btnclear_pressed()
        c.btn4_pressed()
        c.btn9_pressed()
        c.btnsqrt_pressed()
        self.assertEqual(c.btnequal_pressed(), "7.0")
        
    def test_square_root_and_round(self):
        c = Calculator()
        c.btnclear_pressed()
        c.btn7_pressed()
        c.btn1_pressed()
        c.btnsqrt_pressed()
        c.btnround_pressed()
        self.assertEqual(c.btnequal_pressed(), "8")
       
    def test_natural_number(self):
        c = Calculator()
        c.btnclear_pressed()
        c.btne_pressed()
        self.assertEqual(c.btnequal_pressed(), "2.718281828459045")

    def test_natural_number2(self):
        c = Calculator()
        c.btnclear_pressed()
        c.btn5_pressed()
        c.btnplus_pressed()
        c.btne_pressed()
        self.assertEqual(c.btnequal_pressed(), "7.718281828459045")

    def test_modulus(self):
        c = Calculator()
        c.btnclear_pressed()
        c.btn1_pressed()
        c.btn9_pressed()
        c.btnmod_pressed()
        c.btn5_pressed()
        self.assertEqual(c.btnequal_pressed(), "4")
    

if __name__ == "__main__":
    unittest.main()
