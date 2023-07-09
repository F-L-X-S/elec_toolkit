from Loc_curve import *
from  Phys_unit import *
from  Complex_phys_unit import *

#This example shows, how to plot the impedance-locus-curve of a resistor (R1 = 200 Ohm) in series with an
# RC parallel circuit (R2 = 400 Ohm, C=79,6nF) depending to the frequency f

#define the physical values 
R1 = Phys_unit(200, "Ω", "R1")
R2 = Phys_unit(400, "Ω", "R2")
C1 = Phys_unit(79.6*10**(-9), "F", "C1")

#define list with values for mutable variable (in this case: frequency from 1kHz to 8kHz)
frequency_list = list(range(0, 1000000, 10))

#define dict with values for lables and the comments
frequency_labels= {"1kHz": 1000,"2kHz": 2000,"4kHz": 4000, "6kHz": 6000, "8kHz": 8000, "10kHz": 10000, "∞":1000000}

#define from Locus_curve derived class for the impedance of the circuit
class Impedance(Locus_curve): 
    #define the calculation rule, that returns the complex value for a single value of the mutable variable 
    def calc_rule(self, frequency):
        return self.R_ser + 1/((1/self.R_par)+(2*np.pi*frequency*self.C_par)*1j)
    def __init__(self, R_ser, R_par, C_par, frequency_list):
        self.R_ser = R_ser
        self.R_par = R_par
        self.C_par = C_par
        #__init__("Plot-title", "descr. of the result", "descr. of mutable variable", list with values for mutable varaible)
        super().__init__(f"Locus-curve for R-RC-Circuit", f"Z [Ω]", f"f [Hz]", frequency_list)
        
#create the locus curve
impedance_curve = Impedance(R1, R2, C1, frequency_list)
#add the labels and plot the locus curve
impedance_curve.plot_complex(frequency_labels)
#plot amplitude response
impedance_curve.plot_magn(x_log=True, y_log=True)
#plot phase responde 
impedance_curve.plot_phase(x_log=True)