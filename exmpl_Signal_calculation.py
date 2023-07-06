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
const_voltage = dc_signal(time_list, 2*np.pi,"V", "DC-voltage") 
sine = sin_signal(time_list, 2*np.pi, "V", "sine-voltage")

#plot the sine signal with user defined plot parameters
sine.plot(xlim=(0, 2*np.pi), x_steps=list(np.arange(0, 2*np.pi, 0.25*np.pi)), ylim=(-1.5, 1.5), y_steps=list(np.arange(-1.5, 1.75, 0.25)), 
          title = "sine signal",linewidth=2.0, color = 'g')

#calculate new signal 
delayed_sine = sine + const_voltage
#plot the calculated signal with calculated plot parameters 
delayed_sine.plot(linestyle = ":",color = "r")

#create Signal from multiple harmonics (two-pulse rectifier signal)
class harmonics_signal(Signal):
        def calc_rule(self, angle):
            for n in range(0, 21):
                
            return np.sin(angle)