
# coding: utf-8

# ## Importing numpy and creating an array

# In[2]:

import numpy as np
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)
print(type(a))
print(a.shape)


# ## Quickly define special arrays

# In[12]:

b = np.zeros((4,4),dtype=np.float)
print(b)
c = np.ones((4,3),dtype=np.int)
print(c)
d = np.eye(3,dtype=np.float)
print(d)
e = np.reshape(np.arange(10),(2,5))
print(e)


# ## Array slicing

# In[20]:

x = np.arange(10)
print(x)
x1 = x[2:8]
print(x1)


# ## Broadcasting

# In[26]:

a = np.array([12,13,14])
print(a+3)
print(a.mean(),a.sum())


# ## Vectorization

# In[29]:

a = np.arange(5)**3
print(np.sqrt(a))


# ## Masking

# In[50]:

a = np.random.rand(10).reshape((2,5))
b = np.logical_and((a>0.1),(a<0.5))
print(b)
print(a[b])


# ## Challenge: Linear Algebra

# In[56]:

A = np.array([[1,1,1],[0,2,5],[2,5,-1]])
b = np.array([6,-4,27])
if np.linalg.det(A) == 0.0:
    print("No unique solution exists")
else:
    x = np.linalg.solve(A,b)
    print("Solution is: ",x)


# In[ ]:



