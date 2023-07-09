from copy import deepcopy
#________________________Phys_unit________________________
#defines a real value with unit and optional description
#e.g.: R1 = Phys_unit(104, "Ω", "Resistor R1")

class Phys_unit():
    unit: str
    descr: str
        
    def __init__(self, value, unit, description=""):
        if issubclass(type(value), Phys_unit) == True:
            self.value = value.value
        else: 
            self.value = value
        self.unit = unit
        self.descr = description
        
    def __call__(self):
            return self.value
        
    def __str__(self): 
        return f"{self.descr} : {self.value} {self.unit}"
    
    def __add__(self, other): 
        if issubclass(type(other), Phys_unit) == True:
            ret_instance = deepcopy(self)
            ret_instance.value = self.value + other.value
            return ret_instance
        else:
            return self.value + other
    
    def __radd__(self, other): 
         return other+self.value  
        
    def __sub__(self, other): 
        if issubclass(type(other), Phys_unit) == True:
            ret_instance = deepcopy(self)
            ret_instance.value = self.value - other.value
            return ret_instance
        else:
            return self.value - other
    
    def __rsub__(self, other): 
            return other-self.value  
    
    def __mul__(self, other):
        ret_instance = deepcopy(self)
        if issubclass(type(other), Phys_unit) == True:
            ret_instance.value = self.value * other.value
            return ret_instance
        else: 
            ret_instance.value = self.value * other
            return ret_instance
    
    def __rmul__(self, other):
        ret_instance = deepcopy(self)
        ret_instance.value = other * self.value
        return ret_instance
        
    def __truediv__(self, other):
        ret_instance = deepcopy(self)
        if issubclass(type(other), Phys_unit) == True:
            ret_instance.value = self.value / other.value
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
        
    def __round__(self, other):
        ret_instance = deepcopy(self)
        ret_instance.value = round(self.value, other)
        return ret_instance