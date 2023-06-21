import numpy as np
from Phys_unit import Phys_unit
from copy import deepcopy

class Signal(Phys_unit):
    #define calculation in derived class
    def calc_rule(self, angle):
        pass
    
    def __init__(self, times: list, period: float, unit: str, discription=""):  
        data = {}
        #periodic Signal
        if period != 0.0: 
            frequency = 1/period
            for t in  times: 
                t = round(t, 6)
                angle = round(2*np.pi*frequency*t, 6)
                data[t] = round(self.calc_rule(angle), 6)   
        #constant signal
        else:
            for t in  times: 
                t = round(t, 6)
                data[t] = round(self.calc_rule(0), 6)   

        super().__init__(data, unit, discription)  
    
    def __call__(self, t=None):
        if t == None:
            return self.value
        else:
            t = round(t, 6)
            return (self.value[t])
    
    def __add__(self, other): 
        res_signal = deepcopy(self)
        if type(other) == Phys_unit or type(other) == float or type(other) == int: 
            for t, value in self.value.items():
                res_signal.value[t] = value + other
        elif isinstance(other, Signal) == True:
            for t, value in self.value.items():
                res_signal.value[t] = value + other.value[t]
        else:
            return None
        return res_signal
    
    def __radd__(self, other): 
         return self.__add__(other)
        
    def __sub__(self, other): 
        res_signal = deepcopy(self)
        if type(other) == Phys_unit or type(other) == float or type(other) == int: 
            for t, value in self.value.items():
                res_signal.value[t] = value - other
        elif isinstance(other, Signal) == True:
            for t, value in self.value.items():
                res_signal.value[t] = value - other.value[t]
        else:
            return None
        return res_signal
    
    def __rsub__(self, other): 
        res_signal = deepcopy(self)
        if type(other) == Phys_unit or type(other) == float or type(other) == int: 
            for t, value in self.value.items():
                res_signal.value[t] = other - value
        elif isinstance(other, Signal) == True:
            for t, value in self.value.items():
                res_signal.value[t] = other.value[t] - value
        else:
            return None
        return res_signal
    
