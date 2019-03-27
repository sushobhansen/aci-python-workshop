
# coding: utf-8

# ## Defining variables

# In[1]:

x = 1.0
y = 'Hello, World!'
z = (x==y)
print(type(x),type(y),type(z),z)


# ## Mutability

# In[2]:

x = 1
print(id(x))
x = 2.0
print(id(x))


# In[3]:

x = (1,2,3)
x[0] = 10
print(x)


# In[4]:

x = [1,2,3]
print(id(x))
x[0] = 10
print(id(x))
print(x)


# ## Operations

# In[5]:

x = 2
print(x+2)
print(x+2.5)
print('Goodbye'+'Hello')
print(x+'Hello')


# In[6]:

x = 2
print(str(x)+'Hello')


# In[ ]:



