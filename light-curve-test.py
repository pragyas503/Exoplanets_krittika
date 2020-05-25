# -*- coding: utf-8 -*-
"""
Created on Sun May 24 00:14:16 2020
@author: Ranjan
"""
import numpy as np
import matplotlib.pyplot as plt

#%%
x=np.zeros(300)
x+=1
t=np.linspace(1,300,300)
b=np.linspace(-25,25,50)
x[100:150]*=np.square(b/25)
x+= 0.25*np.random.randn()
plt.scatter(t, x, s=3)
#%%#%%
def lin_func(x,m,c):
    return m*x + c 
    return 
xdata = np.arange(0,25,0.1)
ydata = lin_func(xdata,1.2,1.5) + 0.2 * np.random.randn(len(xdata))
plt.scatter(xdata,ydata, s=1)

for i in range(5):
    x_temp=np.copy(x)
    x_temp+=np.random.rand()
    plt.scatter(t, x_temp, s=3)
    
#%%
y=np.zeros(30)
y+=1
t=np.linspace(1,30,30)

y[14:21]=0.996

for i in y(10,15):
    dy=(y[15]-y[10])/(15-10)
    n=1
    y= y+ n*dy
    n+=n
    
#dy= (y[10]-y[14])/3
#y[11]= y[11]-dy
#y[12]= y[12]- 2*dy
#y[13]= y[13]-3*dy
#y[19]= y[19]+dy
#y[20]= y[20]+2*dy

#y[11]=np.average(y[10:12])
#y[19]=np.average(y[18:20])
#x+= 0.3*np.random.randn()
plt.plot(t,y)
#plt.scatter(t, x, s=3)


#%%

def line_fn(x1,y1,x2,y2,x):
    return y1 + ((y2-y1)/(x2-x1))*(x-x1)

t= np.arange(0,30,1)
y= np.zeros(30)
y+=1

for i in y:
    if i<=10:
        y+=1
    elif i>10 and i<=15:
        y= line_fn(t[10],1,t[15],0.995,t)
    elif i>15 and i<=21:
        y+=0.995
    elif i>21 and i<=25:
        y=line_fn(t[21],0.995,t[25],1,t)
    elif i>26:
        y+=1 
        
        
plt.plot(t,y)