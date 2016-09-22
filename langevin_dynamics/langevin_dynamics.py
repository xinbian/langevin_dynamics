import unittest
import numpy as np
import matplotlib.pyplot as plt

f = open('/home/travis/build/xinbian/langevin_dynamics/langevin_dynamics/potential.d','w')
for i in range(1, 201, 1):
  f.write("%10s  %10s  %10s\n" % (i, np.sin(i), np.cos(i)))
f.close()

#read inout parameter
with open('/home/travis/build/xinbian/langevin_dynamics/langevin_dynamics/input.d', 'r') as f:
       x=f.readline()
       v=f.readline()
       temp=f.readline()
       dampcoeff=f.readline()
       deltat=f.readline()
       totalt=f.readline()
       m=f.readline()
       
x=float(x)
v=float(v)
temp=float(temp)
dampcoeff=float(dampcoeff)
deltat=float(deltat)
totalt=float(totalt)
m=float(m)
time=0
nstep=int(totalt/deltat)

#generate random number
mu, sigma=0, 2*np.sqrt(dampcoeff)*temp
eta=np.random.normal(mu,sigma,nstep)
#count, bins, ignored = plt.hist(eta, 30, normed=True)


f = open('/home/travis/build/xinbian/langevin_dynamics/langevin_dynamics/output.d','w')
for i in range(1, nstep+1):  
    a=(-dampcoeff*v+eta[i-1]-np.cos(x))/m
    v=v+deltat*a
    x=x+v*deltat
    time=time+deltat
    f.write("%3s %5s %10s %10s\n" % (i, time, x, v))
    i=i+1
f.close()
