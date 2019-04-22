import numpy as np
def f(x,y,x0,y0):
    return(((x-x0)**2+(y-y0)**2)**0.5)
x=np.array([[0,1],[0,2]])
y=np.array([[0,0],[1,1]])
x0=2
y0=1
print(f(x,y,x0,y0))
