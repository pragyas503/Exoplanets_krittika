# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 00:51:37 2020

@author: Ranjan
"""
import numpy as np
import matplotlib.pyplot as plt

#Equation of line, when two end coordinates are known i.e.y-y1=m(x-x1)
def line_fn(x1,y1,x2,y2,x):
    return y1 + ((y2-y1)/(x2-x1))*(x-x1)


def limb_dark(typ, dip_dur):
    '''Limb darkening effect, coefficients adopted from Sing,2010'''

    u= 0.65
    a= 0.498
    b= 0.194
    u1=0.701
    u2=-0.664
    u3=1.38
    u4=-0.627
    mu= np.linspace(-np.pi/2,np.pi/2,dip_dur)
    if typ=='Linear':
        return 1- u*(1-np.cos(mu))
    if typ=='Quadratic':
        return 1- a*(1-np.cos(mu))- b*(1-np.cos(mu))**2
    if typ== 'Non-linear':
        return 1- u1*(1-(np.cos(mu))**0.5)- u2*(1-(np.cos(mu))) - u3*(1-(np.cos(mu))**1.5) - u4*(1-(np.cos(mu))**2)

t= np.arange(0,200,1)           #Time

y= np.zeros(200)                #Relevive flux
y[:20]=1
y[20:25]= line_fn(t[20],1,t[25],0.996,t[20:25])
y[25:35]=0.996
y[35:40]=line_fn(t[35],0.996,t[40],1,t[35:40])
y[40:]=1 

norm_flux_l= np.zeros(200)         # Normalised flux with linear limb darkening
norm_flux_l[:20]=y[:20] 
norm_flux_l[20:40]= (y[20:40]/limb_dark('Linear',20))/((y[20:40]/limb_dark('Linear',20)).max())
norm_flux_l[40:]=y[40:]
norm_flux_l[140:160]=norm_flux_l[20:40] 

norm_flux_q= np.zeros(200)        # Normalised flux with quadratic limb darkening
norm_flux_q[:20]=y[:20] 
norm_flux_q[20:40]= (y[20:40]/limb_dark('Quadratic',20))/((y[20:40]/limb_dark('Quadratic',20)).max())
norm_flux_q[40:]=y[40:]
norm_flux_q[140:160]=norm_flux_q[20:40]

norm_flux_nl= np.zeros(200)        # Normalised flux with non-linear limb darkening
norm_flux_nl[:20]=y[:20] 
norm_flux_nl[20:40]= (y[20:40]/limb_dark('Non-linear',20))/((y[20:40]/limb_dark('Non-linear',20)).max())
norm_flux_nl[40:]=y[40:]
norm_flux_nl[40:]=y[40:]
norm_flux_nl[140:160]=norm_flux_nl[20:40] 

plt.figure(figsize=(8,6))
#plt.plot(t,y,label='relative_flux')
plt.plot(t,norm_flux_l,label='Linear')
plt.plot(t,norm_flux_q,label='Quadratic')
plt.plot(t,norm_flux_nl,label='Non-linear')
plt.xlabel('Time in hours')
plt.ylabel('Normalised flux')
plt.title('Transit light curve with limb darkening')
plt.legend()
plt.show()


  