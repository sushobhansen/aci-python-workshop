
# coding: utf-8

# ## Printing function

# In[28]:

def print_input(x):
    print(x)

k = 'Hello'
print_input(k)

j = 'How are you'
print_input(j)

x = 'I am good'
print_input(x)


# ## Add 5 to a list

# In[29]:

def add5(x):
    y = []
    for i in x:
        y.append(i+5)
    return y

a = ['one','two']
b = add5(a)
print(b)


# ## Solve a system of linear eqs in two variables

# In[30]:

def solve_eqs(a,b,c,d,e,f):
    if (a*d-b*c)==0:
        return 'Error'
    x = (d*e-b*f)/(a*d-b*c)
    y = (a*f-c*e)/(a*d-b*c)
    return (x,y)

a = solve_eqs(3.2,3.2,7.8,7.8,1.3,2.4)
print(a)


# ## Default args

# In[31]:

def addnumber(x,n=5):
    y = []
    for i in x:
        y.append(i+n)
    return y

a = range(3)
print(addnumber(a))
print(addnumber(a,n=2))


# In[ ]:



