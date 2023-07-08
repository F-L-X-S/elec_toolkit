from Signal import *
import Complex_phys_unit 

#---------------Create Signal with calculation Rule---------------
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
const_voltage = dc_signal.from_calc_rule(times=time_list, period = 2*np.pi, unit = "V", discription = "DC-voltage") 
sine = sin_signal.from_calc_rule(times=time_list, period = 2*np.pi, unit = "V", discription = "sine-voltage")

#plot the sine signal with user defined plot parameters
#sine.plot(xlim=(0, 2*np.pi), x_steps=list(np.arange(0, 2*np.pi, 0.25*np.pi)), ylim=(-1.5, 1.5), y_steps=list(np.arange(-1.5, 1.75, 0.25)), 
#          title = "sine signal",linewidth=2.0, color = 'g')

#calculate new signal 
delayed_sine = sine + const_voltage
#plot the calculated signal with calculated plot parameters 
#delayed_sine.plot(linestyle = ":",color = "r")

#---------------create Signal from multiple harmonics (two-pulse rectifier signal)---------------
#create harmonics up to 20th
max_amplitude = 5   #Amplitude of 5V
frequency = 1  #Frequency of the resulting Signal (e.g. period of 1s)
harmonics = []
#use the formula of the fourier transformation for the signal specific calculation 
for n in range (0, 21):
    if n == 0: 
        #create complex value with frequency = 0 for DC value 
        harmonics.append(Complex_phys_unit.Complex_phys_unit(complex(2*max_amplitude/np.pi, 0), unit="V", discription=str(n)+"th harmonic", frequency = 0))
    elif n%2 == 0:
        #create complex value with n'th frequency 
        harmonics.append(Complex_phys_unit.Complex_phys_unit(complex(4*max_amplitude/(np.pi*(1-n**2)), 0), unit="V", discription=str(n)+"th harmonic", frequency = n*frequency))
    else:
        harmonics.append(Complex_phys_unit.Complex_phys_unit(complex(0, 0), unit="V", discription=str(n)+"th harmonic", frequency = n*frequency))
#ceate times 
time_list = list(np.arange(0, 1, 1/1000))    
two_pulse_rect = Signal.from_harmonics(harmonics = harmonics,times = time_list, period = 1/frequency, unit = "V", discription="two-pulse rectifier signal")
two_pulse_rect.plot()
