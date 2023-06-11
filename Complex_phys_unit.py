from Phys_unit import *
import numpy as np
import matplotlib.pyplot as plt

class Complex_phys_unit(Phys_unit):
    def __init__(self, value, unit, discription=""):
        self.value = value
        self.unit = unit
        self.discr = discription
        self.magn = round(self.complex_to_polar(value)['magn'], 3)
        self.phase = round(self.complex_to_polar(value)["phase"], 3)
        super().__init__(value, unit, discription)

    @classmethod 
    def from_polar(cls, magnitude, phase, unit, discription=""):
        complex_value = cls.polar_to_complex(magnitude, phase)
        return cls(complex_value, unit, discription)
    
    def __str__(self): 
        return f"{self.discr} : {self.value}{self.unit} = {self.magn}{self.unit}∠{self.phase}°"   
     
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
    