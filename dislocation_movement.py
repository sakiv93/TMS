import numpy as np 
import matplotlib.pyplot as plt 
#To find shear stress as the position changes
def shear_stress(shear_modulus,burgers_vector,poissons_ratio,dx):
    d=shear_modulus*burgers_vector/(2*np.pi*(1-poissons_ratio))
    shear_stress=d/dx
    return shear_stress
#To find velocity as position changes
def velocity(burgers_vector,drag_coefficient,shear_stress):
    velocity =(burgers_vector/drag_coefficient)*shear_stress
    return velocity

#Material properties
shear_modulus=100e9 # Pa
burgers_vector=0.25e-9 #m
poissons_ratio=0.3
drag_coefficient=4e-4 #pa.s
#Time step 
delta_t=1e-10  #s

x0=100.0e-9 #m dislocation 1 in fixed position
x1_old=200.0e-9 #m free moving dislocation initial position

times=[]       #For plotting purpose
positions=[]   #For plotting purpose


#For loop to to iterate over number of steps mentioned above
for i in range(n_steps):
    times.append((i+1)*delta_t)
    positions.append(x1_old)
    distance=x1_old-x0
    shear_stress_1=shear_stress(shear_modulus,burgers_vector,poissons_ratio,distance)
    tau=velocity(burgers_vector,drag_coefficient,shear_stress_1)
    x1_new=x1_old+delta_t*tau
    print(x1_new)
    x1_old=x1_new

plt.plot(times,positions)
plt.xlabel('times[s]')
plt.ylabel('positions [m]')
plt.show()

#To find length of times and positions array for getting idea if x and y points are equal for plotting purpose
print(len(times))
print(len(positions))






