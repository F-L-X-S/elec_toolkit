from Phys_unit import *
import numpy as np
import matplotlib.pyplot as plt

class Complex_phys_unit(Phys_unit):
    def __init__(self, value: complex, unit="", description="", frequency=1):
        self.value = value
        self.frequency = frequency 
        self.unit = unit
        self.descr = description
        self.magn = round(self.complex_to_polar(value)['magn'], 3)
        self.phase = round(self.complex_to_polar(value)["phase"], 3)
        self.origin = 0+0j
        super().__init__(value, unit, description)

    #alternative constructor
    @classmethod 
    def from_polar(cls, magnitude, phase, unit, description=""):
        complex_value = cls.polar_to_complex(magnitude, phase)
        return cls(complex_value, unit, description)
    
    def __str__(self): 
        return f"{self.descr} : {self.value}{self.unit} = {self.magn}{self.unit}∠{self.phase}°"   
     
    @staticmethod    
    def polar_to_complex(magnitude, phase):
        re = round(magnitude * np.cos(np.radians(phase)), 3)
        im = round(magnitude * np.sin(np.radians(phase)), 3)
        return complex(re, im)
    
    @staticmethod
    def complex_to_polar(complex_number):
        try:
            phase = np.degrees(np.arctan2(complex_number.imag, complex_number.real)) 
        except ZeroDivisionError:
            phase = 0
        magn = np.sqrt((complex_number.imag**2)+(complex_number.real**2))
        phase=round(phase, 3)
        magn = round(magn, 3)
        return {"magn":magn, "phase":phase}
    
    #Function to plot vector with annotation 
    @staticmethod
    def plot_vector(vector, origin=[0, 0],name = "", unit = "", **options):
        #calculate absolute vector-end
        vector_end=[vector[0]+origin[0], vector[1]+origin[1]]
        #calculate magnitude
        magn = np.sqrt(((vector_end[0]-origin[0])**2)+((vector_end[1]-origin[1])**2))
        #calculate rel. position of annotations
        annotation_pos = [origin[0]+0.7*(vector_end[0]-origin[0]), origin[1]+0.7*(vector_end[1]-origin[1])]
        offset = ( -0.2*magn,0.1*magn )
        #annotate vector
        plt.annotate(name+ " ["+unit+ "]", (annotation_pos[0],annotation_pos[1]),xycoords='data',
                 xytext=offset, textcoords='offset points')
        #plot vector 
        return plt.arrow(origin[0], origin[1], vector[0], vector[1],
            head_width=0.05*magn, head_length=0.1*magn, length_includes_head=True,
            width=0.002*magn, 
            **options)
    
    
    def plot(self, conc_vector=None, **options):
        if conc_vector == None:
            self.origin = 0+0j
        else:
            self.origin = conc_vector.origin + conc_vector.value
        return self.plot_vector([self.value.real, self.value.imag], [self.origin.real, self.origin.imag], self.descr, self.unit, **options)

    def __call__(self, t = None):
        if t != None:
            return self.value.imag*np.sin(2*np.pi*self.frequency *t)+self.value.real*np.cos(2*np.pi*self.frequency *t)
        else:
            return self.value