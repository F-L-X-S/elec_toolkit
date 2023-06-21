
#________________________Phys_unit________________________
#defines a real value with unit and optional discription
#e.g.: R1 = Phys_unit(104, "Ω", "Resistor R1")

class Phys_unit():
    unit: str
    discr: str
        
    def __init__(self, value, unit, discription=""):
        self.value = value
        self.unit = unit
        self.discr = discription
        
    def __call__(self):
        return self.value
        
    def __str__(self): 
        return f"{self.discr} : {self.value} {self.unit}"
    
    def __add__(self, other): 
        if type(other) == Phys_unit:
            return self.value + other.value
        else:
            return self.value + other
    
    def __radd__(self, other): 
         return self.value + other
        
    def __sub__(self, other): 
        if type(other) == Phys_unit:
            return self.value - other.value
        else:
            return self.value - other
    
    def __rsub__(self, other): 
            return other-self.value  
    
    def __mul__(self, other):
        if type(other) == Phys_unit:
            return self.value * other.value
        else: 
            return self.value * other
    
    def __rmul__(self, other):
            return self.value * other
        
    def __truediv__(self, other):
        if type(other) == Phys_unit:
            return self.value / other.value
        else: 
            return self.value / other
    
    def __rtruediv__(self, other):
            return  other / self.value    
        
    def __pow__(self, other):
        if isinstance(other, Phys_unit):
            return self.value ** other.value
        else: 
            return self.value ** other
    
    def __rpow__(self, other):
            return  other**self.value