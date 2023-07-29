from Phys_unit import *
import numpy as np
import matplotlib.pyplot as plt

class Complex_phys_unit(Phys_unit):
    def __init__(self, value: complex, unit="", description="", frequency=1):
        self.value = value
        self.frequency = frequency 
        self.unit = unit
        self.descr = description
        self.magn = self.complex_to_polar(value)['magn']
        self.phase = self.complex_to_polar(value)["phase"]
        self.origin = 0+0j
        super().__init__(value, unit, description)

    #alternative constructor
    @classmethod 
    def from_polar(cls, magnitude, phase, unit, description=""):
        complex_value = cls.polar_to_complex(magnitude, phase)
        return cls(complex_value, unit, description)
     
    @staticmethod    
    def polar_to_complex(magnitude, phase):
        re = round(magnitude * np.cos(np.radians(phase)), 10)
        im = round(magnitude * np.sin(np.radians(phase)), 10)
        return complex(re, im)
    
    @staticmethod
    def complex_to_polar(complex_number):
        try:
            phase = np.degrees(np.arctan2(complex_number.imag, complex_number.real)) #sine-based phase
        except ZeroDivisionError:
            phase = 0
        magn = np.sqrt((complex_number.imag**2)+(complex_number.real**2))
        phase=round(phase, 10)
        magn = round(magn, 10)
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
    
    #Function for plotting amplitude or phase diagram for List of Complex_phys_unit-objects
    @staticmethod
    def plot_bars(harmonics: list,color = 'r',fig = None):
        if fig == None:
            fig=plt.figure(figsize=(12, 10)) #plotsize   
            
        #amplitude    
        ampl_plot = fig.add_subplot(2, 1, 1) #plotposition in matrix (row, column, position)
        amplitudes = {}
        n = 0
        for h in harmonics:
            amplitudes.update([(str(n), h.complex_to_polar(h())["magn"])]) #add amplitude 
            n += 1
        ampl_plot.bar(list(amplitudes.keys()), list(amplitudes.values()), color = color, width = 0.25, align = "center")
        ampl_plot.set_ylabel('amplitude')
        ampl_plot.set_xlabel('Order of the harmonic')
        ampl_plot.set_title('amplitude')
        ampl_plot.set_xticks(list(amplitudes.keys()))
        ampl_plot.set_yticks(np.arange(0, 7, 0.5))
        ampl_plot.grid()
        
        #phase
        phases = {}
        n = 0
        for h in harmonics:
            phases.update([(str(n), h.complex_to_polar(h())["phase"])]) #add magnitude 
            n += 1
        phase_plot = fig.add_subplot(2, 1, 2)
        phase_plot.bar(list(phases.keys()), list(phases.values()), color = color, width = 0.25)
        phase_plot.set_ylabel('Phase [°el]')
        phase_plot.set_xlabel('Order of the harmonic')
        phase_plot.set_title('phase')
        phase_plot.set_xticks(list(phases.keys()))
        phase_plot.set_yticks(np.arange(-180, 190, 20))
        phase_plot.set_xlim(0, 21)
        phase_plot.grid()
        
        plt.show()
        return 0
  

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

        
    def __str__(self): 
        return f"{self.descr} : {self.value}{self.unit} = {self.magn}{self.unit}∠{self.phase}°"   

    
    def __mul__(self, other):
        ret_instance = deepcopy(self)
        if issubclass(type(other), Complex_phys_unit) == True:
            ret_instance.value = self.value * other.value
            return ret_instance
        elif type(other) == Phys_unit:
            ret_instance.value = complex(self.value.real * other.value, self.value.imag * other.value)
            return ret_instance
        else: 
            ret_instance.value = self.value * other
            return ret_instance
    
    def __rmul__(self, other):
        return self.__mul__(other)
        
    def __truediv__(self, other):
        ret_instance = deepcopy(self)
        if issubclass(type(other), Complex_phys_unit) == True:
            ret_instance.value = self.value / other.value
            return ret_instance
        elif type(other) == Phys_unit:
            ret_instance.value = complex(self.value.real / other.value, self.value.imag / other.value)
            return ret_instance
        else: 
            ret_instance.value = self.value / other
            return ret_instance
    
    def __rtruediv__(self, other):
        ret_instance = deepcopy(self)
        ret_instance.value = other / self.value
        return ret_instance
        
    def __pow__(self, other):
        if issubclass(type(other), Phys_unit) == True:
            ret_instance = deepcopy(self)
            ret_instance.value = self.value ** other.value
            return ret_instance 
        else: 
            ret_instance = deepcopy(self)
            ret_instance.value = self.value ** other
            return ret_instance
    
    def __rpow__(self, other):
            return  other**self.value
