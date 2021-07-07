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
        c.bl_pressed()
        c.btn9_pressed()
        c.btn9_pressed()
        c.btnminus_pressed()
        c.btn3_pressed()
        c.btn6_pressed()
        c.br_pressed()
        c.btndivide_pressed()
        c.btn9_pressed()
        c.btnplus_pressed()
        c.btn3_pressed()
        c.btnmultiply_pressed()
        c.btn6_pressed()
        c.btnmultiply_pressed()
        c.btn1_pressed()
        c.btn0_pressed()
        c.del_pressed()
        self.assertEqual(c.btnequal_pressed(), "25.0")
    
    def test_power(self):
        c = Calculator() 
        c.btnclear_pressed()
        c.btn9_pressed()
        c.pow_pressed()
        c.btn1_pressed()
        self.assertEqual(c.btnequal_pressed(), "9")

    def test_sin(self):
        c = Calculator() 
        c.btnclear_pressed()
        c.btn0_pressed()
        c.sin_pressed()
        self.assertEqual(c.btnequal_pressed(), "0.0")
    
    def test_sin2(self):
        c = Calculator() 
        c.btnclear_pressed()
        c.btn6_pressed()
        c.btn9_pressed()
        c.sin_pressed()
        self.assertEqual(c.btnequal_pressed(), "-0.11478481378318722")
    
    def test_cos(self):
        c = Calculator() 
        c.btnclear_pressed()
        c.btn0_pressed()
        c.cos_pressed()
        self.assertEqual(c.btnequal_pressed(), "1.0") 
    
    def test_cos2(self):
        c = Calculator() 
        c.btnclear_pressed()
        c.btn4_pressed()
        c.btn5_pressed()
        c.cos_pressed()
        self.assertEqual(c.btnequal_pressed(), "0.5253219888177297") 
        
    
    def test_tan(self):
        c = Calculator() 
        c.btnclear_pressed()
        c.btn0_pressed()
        c.tan_pressed()
        self.assertEqual(c.btnequal_pressed(), "0.0") 

    def test_tan2(self):
        c = Calculator() 
        c.btnclear_pressed()
        c.btn5_pressed()
        c.tan_pressed()
        self.assertEqual(c.btnequal_pressed(), "-3.380515006246586") 
        
        
    def test_arcsin(self):
        c = Calculator() 
        c.btnclear_pressed()
        c.btn0_pressed()
        c.btnarcsin_pressed()
        self.assertEqual(c.btnequal_pressed(), "0.0")
    
    def test_arcsin2(self):
        c = Calculator() 
        c.btnclear_pressed()
        c.btn0_pressed()
        c.btndot_pressed()
        c.btn2_pressed()
        c.btn4_pressed()
        c.btn5_pressed()
        c.btnarcsin_pressed()
        self.assertEqual(c.btnequal_pressed(), "0.24751969253381592")
      
    def test_round(self):
        c = Calculator() 
        c.btnclear_pressed()
        c.btn6_pressed()
        c.btn6_pressed()
        c.dot_pressed()
        c.btn1_pressed()
        self.assertEqual(c.round_pressed(), "66") 
    
    def test_logarithm(self):
        c = Calculator() 
        c.btnclear_pressed()
        c.btn1_pressed()
        c.btn0_pressed()
        c.btn0_pressed()
        c.logarithm_pressed()
        self.assertEqual(c.round_pressed(), "2")
    
    def test_par(self):
        c = Calculator
        c.btnclear_pressed(c)
        c.btn1_pressed(c)
        c.btnplus_pressed(c)
        c.bl_pressed(c)
        c.btn3_pressed(c)
        c.btnminus_pressed(c)
        c.btn2_pressed(c)
        c.btnmultiply_pressed(c)
        c.btn4_pressed(c)
        c.br_pressed(c)
        self.assertEqual(c.btnequal_pressed(c), "-4")
    
    def test_ln(self):
        c = Calculator
        c.btnclear_pressed(c)
        c.btn5_pressed(c)
        c.ln_pressed(c)
        self.assertEqual(c.btnequal_pressed(c), "1.6094379124341003")
        
    def test_factorial(self):
        c = Calculator() 
        c.btnclear_pressed()
        c.btn1_pressed()
        c.btn3_pressed()
        c.fact_pressed()
        self.assertEqual(c.btnequal_pressed(), "6227020800")

    def test_square_root(self):
        c = Calculator() 
        c.btnclear_pressed()
        c.btn4_pressed()
        c.btn9_pressed()
        c.sqr_pressed()
        self.assertEqual(c.btnequal_pressed(), "7.0")
        
    def test_square_root_and_round(self):
        c = Calculator()
        c.btnclear_pressed()
        c.btn7_pressed()
        c.btn1_pressed()
        c.sqr_pressed()
        c.round_pressed()
        self.assertEqual(c.btnequal_pressed(), "8")
       

    



if __name__ == "__main__":
    unittest.main()
