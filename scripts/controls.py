
# coding: utf-8

# ## Basic if statement

# In[28]:

x = 6
if x<5:
    print('x is less than 5')
    print('Finished evaluating if block')
print('Finished this code block')


# ## Nested if statements

# In[29]:

x = 6
if x<5:
    print('x is less than 5')
    print('Finished evaluating outer if block')
    
    if x>2:
        print('but x is greater than 2')
        print('Finished evaluating inner if block')
print('Finished this code block')


# ## Condition with logical operator

# In[30]:

x = 6
if x<5 and x>2:
    print('x is less than 5 and greater than 2')
    print('Finished evaluating  if block')
print('Finished this code block')


# ## if-else statement

# In[32]:

x = 6
#Two condition evaluations
if x<5:
    print('x is less than 5')
if x>5:
    print('x is greater than 5')
print('Finished this code block')

#One condition evaluation
if x<5:
    print('x is less than 5')
else:
    print('x is greater than 5')
print('Finished this code block')


# # if-elif-else statement

# In[33]:

x = 6
if x<5:
    print('x is less than 5')
elif x>5:
    print('x is greater than 5')
else:
    print('x is equal to 5')
print('Finished this code block')


# ## while loop

# In[34]:

x = 3
while(x<6):
    print('The value of x is ',x)
    x+=1


# ## simple for loop

# In[35]:

x = range(3)
print(list(x))
for i in x:
    print('The value of i is ',i)


# ## for loop with mixed data types

# In[36]:

for i in ['Harry',(0,1,2),1]:
    print(i)


# ## for loop with multiple variables

# In[37]:

x = [0,1,2]
y = [10,11,12]
z = [21,22,23]
print(list(zip(x,y,z)))
for i,j,k in zip(x,y,z):
    print(i,'+',j,'+',k,'=',i+j)


# ## In-line for loop

# In[3]:

x = [i**2 for i in range(5)]
print(x)


# ## Break, continue, and pass

# In[1]:

for x in range(10):
    if x==3:
        continue
    if x==5:
        pass
    if x==8:
        break
    print(x)


# In[ ]:



