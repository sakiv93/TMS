import numpy as np 
import matplotlib.pyplot as plt 
import math

#Task1

#To find Internal stress around dislocation due to surrounding disloactions 
def get_internal_stress(x_coords,shear_modulus,poissons_ratio,burgers_vector):
    print('Input positions in stress loop:',x_coords)
    d=shear_modulus*burgers_vector/(2*np.pi*(1-poissons_ratio))
    stress=np.array([])
    swap=0
    for j in range(len(x_coords)):
        stress_final=0
        # Use swapping teqnique to find distance between dislocations
        swap=x_coords[j]
        x_coords[j]=x_coords[0]
        x_coords[0]=swap
        for i in range(len(x_coords)-1): #Its is length minus one due to distance calculation is between two points
            stress_iteration=d/(x_coords[0]-x_coords[i+1])
            stress_final=stress_final+stress_iteration
        stress=np.append(stress,stress_final)
    return stress

#To find velocity as position changes
def velocity(burgers_vector,drag_coefficient,shear_stress):
    velocitys=np.array([])
    for i in range(len(shear_stress)):
        velocity =(burgers_vector/drag_coefficient)*shear_stress[i]
        velocitys=np.append(velocitys,velocity)
    return velocitys

# System_Definition
system_length_x= 2e-6 #m
shear_modulus= 26e9 #Pa
poissons_ratio=0.33
burgers_vector=0.256e-9 #m
drag_coefficient=1e-4 #Pa-s
total_time=10e-9 #s
number_steps=50
delta_t=total_time/number_steps
print('Time_step=',delta_t)

#Initial_Values
length= 2e-6 #m
n_dislocations=4
initial_position=length*np.array([0.1,0.13,0.16,0.3]) #x-co-ordinates
final_position=np.array([])
tau=np.array([])
final_position=initial_position #for loop initiating purpose
positions=np.array([initial_position])
times=np.array([0])


#Loop to calculate final positions with time

for i in range(number_steps):
    shear_stress=get_internal_stress(np.copy(final_position),shear_modulus,poissons_ratio,burgers_vector)
    #Here np.copy is used for call by value purpose in order to prevent function modifying outside variable
    #In internl stress calculation function my initial positions get swapped according to requirement.
    tau=velocity(burgers_vector,drag_coefficient,shear_stress)
    print('Tau value in Final position loop:',tau)
    #x1_new=x1_old+delta_t*tau
    final_position=final_position+delta_t*tau
    positions=np.append(positions,[final_position],axis=0)
    times=np.append(times,[(i+1)*delta_t],axis=0)
    print('positions inside positions loop:',positions)
    print('Final_positions in Final position loop:',final_position)
    print('Time_steps in Final position loop',times)
print(positions[3,0])

# To plot values of dislocation movement with time
plt.plot(positions,times)
plt.xlabel('positions [m]')
plt.ylabel('times[s]')
plt.show()






























#Test2
#Test2=round(get_internal_stress(np.array([0,2,3.5,4]),20.,0.3,0.1),8)
#Test2=[round(elem,8) for elem in get_internal_stress(np.array([0,2,3.5,4]),20.,0.3,0.1)]
#print(Test2)


#Test3
#Test3=get_internal_stress(initial_position,shear_modulus,poissons_ratio,burgers_vector)
#Test3=[round(elem,1) for elem in get_internal_stress(np.copy(initial_position),shear_modulus,poissons_ratio,burgers_vector)]
#print('Internal stress',Test3)

#Test4
#Test4=velocity(burgers_vector,drag_coefficient,x)
#print(Test4)

#Test5 new positions
#print('velocity:',tau)
#print('Final_positions',final_position)
#print(i)
