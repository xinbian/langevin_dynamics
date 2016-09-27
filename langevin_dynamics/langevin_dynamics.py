import unittest
import numpy as np
import matplotlib.pyplot as plt

x=0.0
xrange=2000
#f = open('/home/travis/build/xinbian/langevin_dynamics/langevin_dynamics/potential.d','w')
#write the potential file
f = open('potential.d','w')
for i in range(1, xrange+1, 1):
  f.write("%s %10s  %10s  %10s\n" % (i, x, (2.0-2.0*(x-10)**2)**2, -16.0*(x-10)+16.0*(x-10)**3))
  x=x+0.01
f.close()
index=np.arange(xrange,dtype=np.float64)
xpotential=np.arange(xrange,dtype=np.float64)
fpotential=np.arange(xrange,dtype=np.float64)
i=0
for colom in open('potential.d').readlines():
   # index[i]=float(colom.split()[1]) 
    xpotential[i]=float(colom.split()[1])
    fpotential[i]=float(colom.split()[3])
    i=i+1

#read input parameter
#with open('/home/travis/build/xinbian/langevin_dynamics/langevin_dynamics/input.d', 'r') as f:
with open('input.d', 'r') as f:
       x=f.readline()
       v=f.readline()
       temp=f.readline()
       dampcoeff=f.readline()
       deltat=f.readline()
       totalt=f.readline()
       m=f.readline()
# v velocity, x position, temp, temperarure, dampcoeff damp coeffcient, m mass      
x=float(x)
v=float(v)
temp=float(temp)
dampcoeff=float(dampcoeff)
deltat=float(deltat)
totalt=float(totalt)
m=float(m)
time=0

##def nstep
def cacl_nstep(totalt, deltat):
    return int(totalt/deltat)
    
nstep=cacl_nstep(totalt, deltat)

#generate random number
mu, sigma=0, 2*np.sqrt(dampcoeff)*temp
#eta=np.random.normal(mu,sigma,nstep)
#count, bins, ignored = plt.hist(eta, 30, normed=True)

def cacl_random(mu, sigma, nstep):
    x=np.random.normal(mu,sigma,nstep) 
    return x

eta=cacl_random(mu, sigma, nstep)
    
#read potential file
#f = open('/home/travis/build/xinbian/langevin_dynamics/langevin_dynamics/output.d','w')
#main loop
f = open('output.d','w')
for i in range(1, nstep+1):  
    finter=np.interp(x,xpotential,fpotential)
    a=(-dampcoeff*v+eta[i-1]-finter)/m
    v=v+deltat*a
    x=x+v*deltat
    time=time+deltat
    f.write("%4s\t%5s\t%10s\t%10s\n" % (i, time, x, v))
    i=i+1
f.close()

#xvals = np.linspace(0, 2*np.pi, 50)
#yinterp=np.interp(xvals,xpotential,fpotential)

#post processing 

post_t=np.arange(nstep,dtype=np.float64)
post_x=np.arange(nstep,dtype=np.float64)
post_v=np.arange(nstep,dtype=np.float64)
i=0
for colom in open('output.d').readlines():
   # index[i]=float(colom.split()[1]) 
    post_t[i]=float(colom.split()[1])
    post_x[i]=float(colom.split()[2])
    post_v[i]=float(colom.split()[3])
    i=i+1
    
#plt.figure(1)
#plt.plot(post_t, post_x, '-')
#plt.plot(post_t, post_v, 'o')
#plt.xlabel('time')
#plt.ylabel('position')
#plt.savefig('particle_position.pdf')
#plt.figure(2)
#plt.plot(post_t, post_v, '-')
#plt.xlabel('time')
#plt.ylabel('velocity')
#plt.savefig('particle_velocity.pdf')
#plt.show() 


####unit test
class Test_langevin(unittest.TestCase):
     # test nstep cal function
     def test_step(self):
        self.assertEquals(cacl_nstep(1.0, 0.1), 10)
    # test the mean of random number is reasonable or not
     def test_random_mean(self):
        self.assertTrue(np.mean(cacl_random(0,1,1000))<1)
    # test whether the  particle is confined within the potential well which should be by design
     #def test_particle_confiment(self):
        #self.assertTrue(np.abs(x-10)<10)
     
         
        
tests =  unittest.TestLoader().loadTestsFromTestCase(Test_langevin)
unittest.TextTestRunner().run(tests) 