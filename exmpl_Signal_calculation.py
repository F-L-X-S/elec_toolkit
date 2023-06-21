from Signal import *


#define signal specified by redifinig the calculation rule derived from Signal-class
#define sine-signal with magnitude "1"
class sin_signal(Signal):
        def calc_rule(self, angle):
            return np.sin(angle)

#define constant-signal with magnitude "3"
class dc_signal(Signal):
        def calc_rule(self, angle):
            return 3
    
#ceate times (in this case equal to radians)
time_list = list(np.arange(0, 2*np.pi, 0.01*np.pi))
#create period
period = 2*np.pi

#create instance of the signal as a periodic voltage-Signal    
const_voltage = dc_signal(time_list, 2*np.pi,"V", "DC-Voltage") 
sine = sin_signal(time_list, 2*np.pi, "V", "Sine-Voltage")
print(sine(0.2*np.pi))

