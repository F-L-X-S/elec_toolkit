from  Complex_phys_unit import *
from math import ceil, floor, log10

class Locus_curve():
    #define calculation in inheriting class
    def calc_rule(self, inp_value):
        pass
    
    #calculate every complex data point  
    def calc_data(self, mutable_var_list: list):
        data = {}
        for var in  mutable_var_list: 
            calc_result = self.calc_rule(var)
            if issubclass(type(calc_result), Phys_unit):
                data[var]=self.calc_rule(var).value
            else:
                data[var]=self.calc_rule(var)
        return data
    
    #calculate magnitude for every key with complex as variable
    @staticmethod
    def calc_magn(compl_data: dict):
        magn = {}
        for mut_var, value in compl_data.items():
                magn[mut_var]=np.sqrt((value.real**2)+(value.imag**2))
        return magn
    
    #calculate phase for every key with complex as variable
    @staticmethod
    def calc_phase(compl_data: dict):
        phase = {}
        for mut_var, value in compl_data.items():
            try:
                  phase[mut_var] = np.degrees(np.arctan(value.imag/value.real))
            except ZeroDivisionError:
                  phase[mut_var] = 0
        return phase
    
    #calculate log scale in range of given list
    @staticmethod
    def get_log_scale(non_log_list: list, stepwidth=1, base=10, neg_log=-0.01): 
        try: 
            log_min=round(np.emath.logn(base, min(non_log_list)))
        except OverflowError: 
            log_min=0
        try:    
            log_max=round(np.emath.logn(base, max(non_log_list)))
        except OverflowError:
            log_max=0
        if log_min==0: 
            log_min=neg_log
        log_list = [pow(base, round(i,2)) for i in np.arange(log_min, log_max+stepwidth, stepwidth)]
        print(log_min)
        return log_list
    
    #------------------------------------------------------init takes list with values for mutable variable 
    def __init__(self, name, result_name, mut_var_name, mutable_var_list):
        self.data = self.calc_data(mutable_var_list)                                  
        self.name = name
        self.mut_var_name = mut_var_name
        self.res_name= result_name
    #------------------------------------------------------complex-plot-function
    #plot_complex takes dict "labels" with annotations as keys and mutable variable as value
    #e.g.: "50Hz": 50    
    def plot_complex(self, labels={}):
        #convert data
        re=[]
        im=[]
        for complex_value in self.data.values():
            if issubclass(type(complex_value), Phys_unit):
                re.append(complex_value.value.real)
                im.append(complex_value.value.imag)
            else: 
                re.append(complex_value.real)
                im.append(complex_value.imag)
        #convert labels
        labels_data=self.calc_data(labels.values())
        re_mark=[]
        im_mark=[]
        for annotation, mut_var in labels.items():
            complex_value=labels_data[mut_var]
            re_mark.append(complex_value.real)
            im_mark.append(complex_value.imag)
            plt.annotate(annotation, (complex_value.real, complex_value.imag),
                         horizontalalignment='left',
                         verticalalignment='bottom') 
        
        #plot data and labels
        plt.plot(re, im, color = "red")
        plt.scatter(re_mark, im_mark, color = "black", marker = "p")
        plt.title(self.name)
        #rel_space scales edge according to plotsize
        rel_space_re = 0.5*(max(re)-min(re))
        rel_space_im = 0.1*(max(im)-min(im))
        plt.axis([min(re)-rel_space_re, max(re)+rel_space_re, min(im)-rel_space_im, max(im)+rel_space_im])
        plt.gca().set_aspect("equal")
        plt.ylabel('Im')
        plt.xlabel('Re')
        plt.grid()
        plt.show()
        return None        
    
    #------------------------------------------------------magnitude-plot-function                                       
    def plot_magn(self, xticks=[], yticks=[], x_log=False, y_log=False, figure = None):
        #calc dict of magnitudes 
        if not x_log:
            magn_dict =  self.calc_magn(self.data)
        else:
            #calculate logarithmic data for base 10 
            log_data_keys=self.get_log_scale(list(self.data.keys()), 0.1, 10, -2)
            log_data = self.calc_data(log_data_keys)
            magn_dict =  self.calc_magn(log_data)
        #create plot-figure
        if figure == None:
            fig=plt.figure(figsize=(8, 12)) #plotsize
        #create subplot 
        magn_plot = fig.add_subplot(2, 1, 1) #Plotposition (rows, columns, position)
        magn_plot.plot(magn_dict.keys(), magn_dict.values(), linewidth=2.0, label="Magnitude")

        #config axis-ticks
        if xticks!=[] and yticks!=[]:
            magn_plot.set_xticks(xticks)
            magn_plot.set_yticks(yticks)
        elif xticks!=[]:
            magn_plot.set_xticks(xticks)
        elif yticks!=[]:
            magn_plot.set_yticks(yticks)

        #set limits for axis
        y_min = min(list(magn_dict.values()))
        y_max = max(list(magn_dict.values())) 
        #round to next 10th log
        if y_log == True:
            if y_min <= 0:
                y_min = 10**(-6)
            y_min = 10**(floor(log10(y_min)))
            y_max = 10**(ceil(log10(y_max)))
        x_min = min(list(magn_dict.keys()))
        x_max = max(list(magn_dict.keys()))
        magn_plot.set_xlim(x_min, x_max)
        magn_plot.set_ylim(y_min, y_max)
        
        #scale 
        if x_log:
            magn_plot.set_xscale('log')
        if y_log:
            magn_plot.set_yscale('log')
        
        #comments
        magn_plot.set_title(self.name)
        magn_plot.set_ylabel(self.res_name)
        magn_plot.set_xlabel(f"Magnitude {self.mut_var_name}")
        
        #show plot 
        magn_plot.grid()
        plt.show()
        return fig  
    #------------------------------------------------------phase-plot-function
    def plot_phase(self, xticks=[], x_log=False, figure = None):
        #calc dict of of phases 
        if not x_log:
            phase_dict = self.calc_phase(self.data)
        else:
            #calculate logarithmic data for base 10 
            log_data_keys=self.get_log_scale(list(self.data.keys()), 0.1, 10, -2)
            log_data = self.calc_data(log_data_keys)
            phase_dict =  self.calc_phase(log_data)
        
        #create plot-figure
        if figure == None:
            fig=plt.figure(figsize=(8, 12)) #plotsize
        #create subplot 
        phase_plot = fig.add_subplot(2, 1, 1) #Plotposition (rows, columns, position)
        phase_plot.plot(phase_dict.keys(), phase_dict.values(), linewidth=2.0, label="Phase")

        #config axis-ticks
        rel_y_space = 0.2* abs(max(list(phase_dict.values()))-min(list(phase_dict.values())))
        y_min=min(list(phase_dict.values()))-rel_y_space
        y_max=max(list(phase_dict.values()))+rel_y_space
        phase_ticks = range(round(y_min/10)*10, round(y_max/10)*10, 10)
        if xticks!=[]:
            phase_plot.set_xticks(xticks)
        phase_plot.set_yticks(phase_ticks)

        #set limits for axis        
        x_min = min(list(phase_dict.keys()))
        x_max = max(list(phase_dict.keys()))
        phase_plot.set_xlim(x_min, x_max)
        phase_plot.set_ylim(y_min, y_max)
        
        #scale 
        if x_log:
            phase_plot.set_xscale('log')
        
        #comments
        phase_plot.set_title(self.name)
        phase_plot.set_ylabel(self.res_name)
        phase_plot.set_xlabel(f"Phase {self.mut_var_name}")
        
        #show plot 
        phase_plot.grid()
        plt.show()
        return fig  
