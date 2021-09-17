
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
 
from scipy import *
from scipy.integrate import odeint
 
c= 3*(10**8)
F1 = 2*(10**8)
F2 = 0.6
G = 6.67*(10**-11)
M = 1.989*(10**30)
m=1
 
def fonction(S,t):
    r = S[0]
    theta = S[1]
    v = S[2]
    omega = S[3]
 
    dr = v
    dtheta = omega
 
    dv = (F1 - G*M*m) /(m*(r**2)) + r*(dtheta**2)
    dw = F2/(m*(r**3)) - 2*dr*dtheta/r
 
     
    t0 = 0
    tmax = 1*60*60
    npoint = 100000
    t = np.linspace(t0, tmax, npoint) 
 
    x0= 149600000000
    v0= 0.2*c
    theta = np.pi
    omega = 30000
 
    syst_CI=np.array([x0,theta,v0,omega])                  # Tableau des CI
    Sols=odeint(fonction,syst_CI,t)            # Résolution numérique des équations différentielles
 
    x = Sols[:, 0]
    u = Sols[:, 2]
    return (dr,dtheta,dv,dw)
 
    plt.plot(x*np.cos(u),x*np.sin(u), linewidth=0.25)
    plt.show()
