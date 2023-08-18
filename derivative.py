from math import sin, cos, pi
import numpy as np
from matplotlib import pyplot as plt
x=pi/4
h= np.linspace(pi/4,0,100,endpoint=False)
fdh=np.zeros(100)
bdh=np.zeros(100)
cdh=np.zeros(100)
for i in range(100):
    fdh[i]=(sin(x+h[i])-sin(x))/h[i]
    bdh[i]=(sin(x)-sin(x-h[i]))/h[i]
    cdh[i]=(sin(x+h[i])-sin(x-h[i]))/(2*h[i])
efh=np.zeros(100)
ebh=np.zeros(100)
ech=np.zeros(100)
for i in range(100):
    efh[i]=abs(fdh[i]-cos(x))/cos(x)
    ebh[i]=abs(bdh[i]-cos(x))/cos(x)
    ech[i]=abs(cdh[i]-cos(x))/cos(x)
plt.plot(h,efh,'r',h,ebh,'b',h,ech,'g')
plt.legend(['Forward','Backward','Central'])
plt.show()
