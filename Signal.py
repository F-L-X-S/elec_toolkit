import numpy as np
from Phys_unit import Phys_unit
from copy import deepcopy
import matplotlib.pyplot as plt
from math import ceil, floor

class Signal(Phys_unit):
    #------------------------------------------------------calculation rule
    #define calculation in derived class
    def calc_rule(self, angle):
        return self.value[angle]
    
    #------------------------------------------------------constructor
    def __init__(self, times: list, values: list, unit: str, discription=""):  
        data = dict(zip(times, values))
        super().__init__(data, unit, discription) 

    #------------------------------------------------------construct from superimposed harmonics 
    @classmethod 
    def from_harmonics(cls, harmonics: list,times: list, period: float, unit: str, discription=""):
        data = {}
        #calculte timediscrete values
        for t in times:
            for h in harmonics:
               data[t] =+ h(t)  
 
        return cls(list(data.keys()),list(data.values()), unit, discription)
    
    #------------------------------------------------------construct from redefined calculation rule 
    @classmethod 
    def from_calc_rule(cls, times: list, period: float, unit: str, discription=""):
        data = {}
        #periodic Signal
        if period != 0.0: 
               frequency = 1/period
               for t in  times: 
                   t = round(t, 6)
                   angle = round(2*np.pi*frequency*t, 6)
                   data[t] = round(cls.calc_rule(cls, angle), 6)   
        #constant signal
        else:
                for t in  times: 
                    t = round(t, 6)
                    data[t] = round(cls.calc_rule(cls, 0), 6)   
        return cls(list(data.keys()),list(data.values()), unit, discription)
    #------------------------------------------------------operations
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
    
    #------------------------------------------------------plot signal 
    def plot(self, *,xlim = (None, None), ylim = (None, None), x_steps = None, y_steps = None, title = None, **options):
        #check for existing figure or create new 
        try: fig, ax
        except NameError: fig, ax = plt.subplots()
        #configure plot
        if title == None:
            title = self.discr
        options["label"] = self.discr
        ax.plot(self.value.keys(), self.value.values(), **options)

        #limits abscissa
        if xlim == (None, None):
            xlim = (min(self.value.keys()), max(self.value.keys()))
        #steps abscissa, if not given: use ten steps in domain of definition
        if x_steps == None:
            x_steps = list(self.value.keys())
            x_steps = x_steps[::(int(len(x_steps)/10))]
        #limits for ordinate
        if ylim == (None, None):
            ylim = (floor(min(self.value.values())), ceil(max(self.value.values())))
        #steps ordinate, if not given: use ten steps in value range
        y_step = (ylim[1]-ylim[0])/10
        if y_steps == None:
            y_steps = np.arange(ylim[0]-y_step, ylim[1]+y_step, y_step) 
            
        #increase ordinate limits by one step
        ylim = (ylim[0]-y_step, ylim[1]+y_step)
        
        ax.set(xlim=xlim, xticks=x_steps, ylim=ylim, yticks=y_steps)
        plt.title(title)
        plt.xlabel("t")
        plt.ylabel(self.discr +" [" + self.unit+ "]")
        plt.grid()
        plt.show()
