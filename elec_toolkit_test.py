from elec_toolkit import *
import unittest

#______________________________________________________________________________________________Test Phys_unit class
class Test_Phys_unit(unittest.TestCase):
    def test_add(self):
        R1 = Phys_unit(104, "Ω")
        R2 = Phys_unit(70 * 10**(-3), "Ω")
        sum = (R1 + R2)
        self.assertEqual(sum.value, (R2.value + R1), f"solution of add and radd should be equal: {sum} != {R2.value + R1}")
        self.assertEqual(str(sum), str(Phys_unit(104.07, "Ω")), f"wrong solution of add and radd: {sum}")
        
    def test_sub(self):
        R1 = Phys_unit(104, "Ω")
        R2 = Phys_unit(70 * 10**(-3), "Ω")
        diff = (R1 - R2)
        self.assertEqual(diff.value, ((-R2.value) + R1), "solution of sub and rsub should be equal")
        self.assertEqual(str(diff), str(Phys_unit(103.93, "Ω")), "wrong solution of sub and rsub")
        
    def test_mul(self):
        R1 = Phys_unit(104, "Ω")
        R2 = Phys_unit(70 * 10**(-3), "Ω")        
        mul = R1*R2
        self.assertEqual(str(mul), str(R2.value * R1), "solution of mul and rmul should be equal")
        self.assertEqual(round(mul,5).value, 7.28, "wrong solution of mul and rmul")    
    
    def test_tdiv(self):
        R1 = Phys_unit(104, "Ω")
        R2 = Phys_unit(70 * 10**(-3), "Ω")
        div = R1/R2
        self.assertEqual(str(div), str((R1.value*(1/R2))), "solution of div and multiplication with 1/x should be equal")
        self.assertNotEqual(str(div), str((R2.value/R1)), "solution of div and rdiv should not be equal")
        self.assertEqual(str(round(div, 5)), str(Phys_unit(1485.71429, "Ω")), "wrong solution of div and rdiv")    
        
    def test_pow(self):
        R1 = Phys_unit(104, "Ω")
        pow = R1**3
        self.assertEqual(str(pow), str(R1*R1*R1), "solution of x^3 should be the same as x*x*x")    
        R2 = Phys_unit(70 * 10**(-3), "Ω")
        rpow = 3**R2
        self.assertEqual(round(rpow, 6), 1.079937, "solution of 3^x is wrong") 
        
    def test_str(self): 
        Rm1 = Phys_unit(2400 * 10**3, "A/Vs")
        N1 = Phys_unit(4008, "")
        L1 = Phys_unit(((N1**2)/Rm1), "H", "Inductance primary coil L1")
        self.assertEqual(str(L1), 'Inductance primary coil L1 : 6.69336 H', f"Printed str not as expected: {str(L1)}")

#______________________________________________________________________________________________TestTest Complex_phys_unit Class
class Test_Complex_phys_unit(unittest.TestCase):
    
    def test_from_polar(self):
        Z1 = complex(100, 100)
        from_complex_val = Complex_phys_unit(Z1, "Ω", "Z1 (Inp. Impedance for idle)")
        from_polar_val = Complex_phys_unit.from_polar(np.sqrt((Z1.real**2)+(Z1.imag**2)), 45, "Ω", "Z1 (Inp. Impedance for idle)")
        self.assertEqual(from_complex_val.value, from_polar_val.value, "from polar values constructed object is not equal to regular complex object")
        self.assertEqual(from_complex_val.magn, from_polar_val.magn, "from polar values constructed object is not equal to regular complex object")
        self.assertEqual(from_complex_val.phase, from_polar_val.phase, "from polar values constructed object is not equal to regular complex object")
        self.assertEqual(from_complex_val.unit, from_polar_val.unit, "from polar values constructed object is not equal to regular complex object")
        self.assertEqual(from_complex_val.discr, from_polar_val.discr, "from polar values constructed object is not equal to regular complex object")
        
    def test_str(self):
        complex_val = Complex_phys_unit(complex(-100, 100), "Ω", "complex value")
        self.assertEqual(str(complex_val), 'complex value : (-100+100j)Ω = 141.421Ω∠135.0°', "Printed str not as expected")
        
    def test_polar_to_complex(self):
        Z = [complex(100, 100), complex(-100, 100), complex(-100, -100), complex(100, -100)] 
        phases = [45, 135, -135, -45]
        phase_i = iter(phases)
        magn = np.sqrt((Z[1].real**2)+(Z[1].imag**2))
        sector = 1
        for compl_val in Z:
            phase = next(phase_i)
            self.assertEqual(Complex_phys_unit.polar_to_complex(magn, phase), compl_val, f"from polar to compl. transformed value is not correct in sector {sector}")
            sector +=1

    def test_complex_to_polar(self):
        Z = [complex(100, 100), complex(-100, 100), complex(-100, -100), complex(100, -100)] 
        phases = [45, 135, -135, -45]
        phase_i = iter(phases)
        magn = round(np.sqrt((Z[1].real**2)+(Z[1].imag**2)), 3)
        sector = 1
        for compl_val in Z:
            phase = next(phase_i)
            self.assertEqual(Complex_phys_unit.complex_to_polar(compl_val)["magn"], magn, f"from compl. to polar transformed magn is not correct in sector {sector}")
            self.assertEqual(Complex_phys_unit.complex_to_polar(compl_val)["phase"], phase, f"from compl. to polar transformed phase is not correct in sector {sector}")
            sector +=1

#______________________________________________________________________________________________Test Signal Class
time_list = list(np.arange(0, 2*np.pi, 0.01*np.pi))

class sin_signal(Signal):
        def calc_rule(self, angle):
            return np.sin(angle)
        
class double_sin_signal(Signal):
        def calc_rule(self, angle):
            return 2*np.sin(angle)
        
#define constant-signal with magnitude "3"
class const_signal(Signal):
        def calc_rule(self, angle):
            return 3
    
sine = sin_signal(time_list, 2*np.pi,"V", "Sine")
double_sine = double_sin_signal(time_list, 2*np.pi, "V", "Doubled sine")
const_v_signal = const_signal(time_list, 0, "V", "DC-Voltage")

class Test_Signal(unittest.TestCase):

    def test_constructor(self):
        self.assertEqual(str(double_sine(np.pi/2)), "2.0", "wrong solution for doubled sine")
    
    def test_add(self):
        for t in time_list:
            self.assertEqual(round((sine + sine)(t), 4), round(double_sine(t), 4), "invalid solution of adding two Signal-instances (not equal to double_sine)")
        self.assertEqual(((sine + sine)(np.pi/2)), 2, "invalid solution of adding two Signal-instances")               
        self.assertEqual(((sine + 1)(np.pi/2)), 2, "invalid solution of adding Signal-instance and other (__add__)")  
        self.assertEqual(((sine + const_v_signal)(np.pi/2)), 4, "invalid solution of adding Sine-Signal-instance and to const Signal instance (__add__)") 
        self.assertEqual(((1 + sine)(np.pi/2)), 2, "invalid solution of adding other and Signal-instance (__radd__)") 

    def test_sub(self):
        for t in time_list:
            self.assertEqual(round((sine - double_sine)(t), 4), round(-sine(t), 4), "invalid solution of substracting two Signal-instances")
        self.assertEqual(((sine - double_sine)(np.pi/2)), -1, "invalid solution of substracting two Signal-instances") 
        self.assertEqual(((sine - 1)(np.pi/2)), 0, "invalid solution of sub. int from Signal-instance") 
        self.assertEqual(((1 - sine)(np.pi/2)), 0, "invalid solution of sub. Signal-instance from int (__radd__)") 
#---------------------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()