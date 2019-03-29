
# coding: utf-8

# ## Plotting 1D Data - Bar Plot

# In[16]:

import numpy as np
from matplotlib import pyplot as plt

barnumber = np.arange(4)+1
barheight= np.random.uniform(5.0,10.0,(4,))

plt.bar(barnumber,barheight)
plt.xlabel('Bar Number')
plt.ylabel('Bar Height')
plt.title('Random Bar Heights')
plt.ylim([0,10])
plt.xticks(barnumber)
plt.show()


# ## Plotting 2D data - line plot

# In[27]:

x = np.linspace(0,360,1000)
y = (np.sin(x*np.pi/180.) + np.cos(x*np.pi/180.))/2.0
plt.plot(x,y)
plt.grid()
plt.xlabel('x (degrees)')
plt.ylabel('f(x)')
plt.show()


# ## Plotting 2D data - logarithmic graph

# In[33]:

x = np.linspace(0.,2.,1000)
y1 = np.exp(-x)
y2 = np.exp(-2.0*x)

plt.semilogy(x,y1,label='$e^{-x}$')
plt.semilogy(x,y2,label='$e^{-2x}$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(which='both')
plt.show()


# ## Plotting 2D data - external data file

# In[41]:

hour,temperature,precip_prob = np.loadtxt('../data/weather.csv',dtype=np.float,delimiter=',',skiprows=1,unpack=True)

plt.subplot(1,2,1)
plt.plot(hour,temperature)
plt.xlabel('Hour')
plt.ylabel('Temperature ($^o$F)')
plt.title('Temperature')

plt.subplot(1,2,2)
plt.bar(hour,precip_prob)
plt.xlabel('Hour')
plt.ylabel('Probability (%)')
plt.title('Probability of Precipitation')
plt.show()


# ## Plotting 3D data - full 3D plot

# In[60]:

from mpl_toolkits import mplot3d

x = np.linspace(-6,6,100)
y = np.linspace(-6,6,100)

X,Y = np.meshgrid(x,y)
Z = np.sin(np.sqrt(X**2+Y**2))

fig = plt.figure()
ax = plt.axes(projection='3d')

ax.contour3D(X, Y, Z, 50, cmap='spring')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f(x,y)')
plt.show()


# ## Plotting 3D data - contour file

# In[61]:

plt.contourf(X,Y,Z,50,cmap='spring')
plt.xlabel('x')
plt.ylabel('y')
plt.colorbar(label='f(x,y)')
plt.show()


# In[ ]:



