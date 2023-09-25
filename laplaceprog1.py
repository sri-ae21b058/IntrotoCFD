import numpy as np
from matplotlib import pyplot as plt
def check_convergence(u, u_old, e):
    return np.linalg.norm(u-u_old) < e
nx=ny=65
dx=dy=1.0/(nx)
e=10**-5
x,y=np.mgrid[0.:1.:65j,0.:1.:65j]
phi=x*x-y*y
phi[1:-1,1:-1]=0
count=0
while True:
    phi_old=phi.copy()
    for i in range(1, ny-2):
        for j in range(1, nx-2):
            phi[i, j] = 0.25 * (phi[i + 1, j] + phi[i - 1, j] + phi[i, j + 1] + phi[i, j - 1])
    count+=1
    if check_convergence(phi, phi_old, e):
        break
    else:
        continue

#to write phi and error wrt to x^2-y^2 to a file
f=open('phi.txt','w')
for i in range(nx):
    for j in range(ny):
        f.write(str(phi[i,j])+' ')
    f.write('\n')
f.close()
f=open('error.txt','w')
for i in range(nx):
    for j in range(ny):
        f.write(str(phi[i,j]-x[i,j]*x[i,j]+y[i,j]*y[i,j])+' ')
    f.write('\n')
f.close()
print (count)