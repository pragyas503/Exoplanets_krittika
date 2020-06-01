# -*- coding: utf-8 -*-
"""
Created on Sun May 24 22:57:48 2020

@author: Pragya

Light curve as a piece-wise linear function

Assumed values:
    Mass of the star: 1.5 times sun = 1.5*1.989 × 10^30 kg
    Radius of the star: 5 times sun = 5*6.95700×10^8 m
    
"""
import numpy as np
import matplotlib.pyplot as plt

#Equation of line, when two end coordinates are known i.e.y-y1=m(x-x1)
def line_fn(x1,y1,x2,y2,x):
    return y1 + ((y2-y1)/(x2-x1))*(x-x1)

t= np.arange(0,200,1)           #Time
y= np.zeros(200)                #Relevive flux

#creating piecewise linear fn for relative flux, assuming constant relative flux from star=1, and during transit=0.996
y[:20]=1
y[20:25]= line_fn(t[20],1,t[25],0.996,t[20:25])
y[25:35]=0.996
y[35:40]=line_fn(t[35],0.996,t[40],1,t[35:40])
y[40:]=1 

y[140:160]=y[20:40]             #copying similar value for the next transit
y= y+ 0.00009 * np.random.randn(len(t))        

plt.figure(figsize=(8,6))
plt.scatter(t,y,s=3)
plt.xlabel('Time in hours')
plt.ylabel('Relative flux')
plt.title('Transit light curve')

'''Values obtained form the graph'''
delta= 1-0.996
tF= 10
tT= 20
P= 150-30          #120 hrs i.e. 5days

G= 6.67*10**-11     #Gravitational Constant.

Ms= 1.5* 1.989*10**30       #Mass of star, assumed as 1.5 times star


a= ((P**2*G*Ms)/(4*np.pi**2))**(1/3)         #Semi-major axis

n= (np.square(np.sin(tF*np.pi/P)))/(np.square(np.sin(tT*np.pi/P)))      #intermidiate term to calculate impact parameter 

b= np.sqrt(((np.square(1-np.sqrt(delta)))-n*(np.square(1+np.sqrt(delta))))/(1-n))   #impact parameter

a_Rs= np.sqrt((np.square(1-np.sqrt(delta))-(b**2)*(1-(np.square(np.sin(tT*np.pi/P)))))/(np.square(np.sin(tT*np.pi/P))))  # a/Rs parameter

Rs= a/a_Rs                                 #Radius of star
Rp= Rs*np.sqrt(delta)                      #Radius of planet
rho_s= (32*P/(G*np.pi))*((delta**(3/4))/((np.square(tT))-(np.square(tF)))**(3/2))    #Stellar density 

i= np.arccos(b*Rs/a)                          #orbital inclination

print('Mass of star: {} kg.\nRadius of star: {} m.\nRadius of planet: {} m.\nSemi-major axis: {} m. \nImpact parameter: {}.\nStellar density: {} kg/m^3. \nOrbital inclination: {} degree'.format(Ms,Rs,Rp,a,b,rho_s,i))



