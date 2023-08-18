import numpy as np
from matplotlib import pyplot as plt
def check_convergence(u, u_old, e):
    return np.linalg.norm(u-u_old) < e
nx=ny=64
dx=dy=1.0/(nx-1)
x = np.linspace(0, (nx - 1) * dx, nx)
y = np.linspace(0, (ny - 1) * dy, ny)
X, Y = np.meshgrid(x, y)
e=10**-4
phi=np.zeros((nx,ny))
for i in range(nx):
    phi[i,ny-1]=i*dx*i*dx-1
for i in range(ny):
    phi[nx-1,i]=1-i*dx*i*dx
    phi[0,i]=-i*dx*i*dx
phi_old=np.zeros((nx,ny))
count=0
while check_convergence(phi,phi_old,e)==False:
    phi_old=phi.copy()
    for i in range(1, ny - 1):
        for j in range(1, nx - 1):
            phi[i, j] = 0.25 * (phi[i + 1, j] + phi[i - 1, j] + phi[i, j + 1] + phi[i, j - 1])
    count+=1

sol=np.zeros((nx,ny))
for i in range(nx):
    for j in range(ny):
        sol[i,j]=X[i,j]*X[i,j]-Y[i,j]*Y[i,j] #analytical solution

print (sol-phi)
print (count)