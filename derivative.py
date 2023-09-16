from math import sin, cos, pi
import numpy as np
from matplotlib import pyplot as plt
x=pi/4
n=100
h= [x]
for i in range(n-1):
    h.append(h[i]/2)
fdh=np.zeros(n)
bdh=np.zeros(n)
cdh=np.zeros(n)
for i in range(n):
    fdh[i]=(sin(x+h[i])-sin(x))/h[i]
    bdh[i]=(sin(x)-sin(x-h[i]))/h[i]
    cdh[i]=(sin(x+h[i])-sin(x-h[i]))/(2*h[i])

efh=np.zeros(n)
ebh=np.zeros(n)
ech=np.zeros(n)
for i in range(n):
    efh[i]=abs(fdh[i]-cos(x))/cos(x)
    ebh[i]=abs(bdh[i]-cos(x))/cos(x)
    ech[i]=abs(cdh[i]-cos(x))/cos(x)

plt.figure(1)
plt.plot(h,efh,'r',h,ebh,'b',h,ech,'g')
plt.legend(['Forward','Backward','Central'])
plt.show()

plt.figure(2)
plt.loglog(h,efh,'r',h,ebh,'b',h,ech,'g')
plt.legend(['Forward','Backward','Central'])
plt.show()
