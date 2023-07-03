from Complex_phys_unit import *

#This example shows, how to plot complex values as a vector diagram with the Complex_phys_unit class

#create voltage-objects from magnitude and phase 
V1 = Complex_phys_unit.from_polar(60, 0, "V", "V1")
V2 = Complex_phys_unit.from_polar(60, -120, "V", "V2")
V3 = Complex_phys_unit.from_polar(60, +120, "V", "V3")

#create current-object from real- and imaginary part
I1 = Complex_phys_unit(10+20j, "A", "I1")

#plot the first vector with origin [0, 0]
V1.plot() 
#concatenate the second vector with the previous one 
V2.plot(V1) 
#concatenate the second vector with the previous one 
V3.plot(V2)

X = V1+I1
X.plot()
#plot the current without concatenation
print(I1)
#configure plot (check matplotlib-docs for details)
plt.title("three-phase system")
plt.ylabel('Im')
plt.xlabel('Re')
plt.grid()
plt.gca().set_aspect("equal")
plt.show()
