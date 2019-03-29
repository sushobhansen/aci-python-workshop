
# coding: utf-8

# ## Problem statement
# In this problem, you are required to define a function prime_check() that takes in an integer, and prints "This is a prime number" if it is a prime number, and "This is not a prime number" otherwise. The algorithm is as follows:
# 
# - Negative integers and zero are invalid inputs
# - If the number is 1 or 2, it's a prime number
# - For other numbers, divide it sequentially by each number between 2 and *half* the number
# - If, during the above process, the remainder is *ever* zero, it is not a prime number, otherwise it is

# ## Simple solution

# In[7]:

def prime_check(x):
    '''
    Prints a message indicating if x is a prime number or not
    If x is invalid (negative integer or zero), prints a message
    x is of type int
    '''
    if x<=0:
        print("Invalid")
    elif x==1 or x==2:
        print("This is a prime number")
    else:
        if is_prime(x):
            print("This is a prime number")
        else:
            print("This is not a prime number")

def is_prime(x):
    '''
    Checks if a valid input x is a prime number
    Returns True is x is prime
    Returns False is x is not prime
    x is of type int
    '''
    prime = True
    
    for y in range(2,(x//2)+1):
        if x%y == 0:
            prime = False
            break
    
    return prime

prime_check(1373)


# ## Complicated solution

# In[24]:

def prime_check(x):
    '''
    Prints a message indicating if x is a prime number or not
    If x is invalid (negative integer or zero), prints a message
    x is of type int
    '''
    if x<=0:
        print("Invalid")
    elif x==1 or x==2:
        print("This is a prime number")
    else:
        if is_prime(x):
            print("This is a prime number")
        else:
            print("This is not a prime number")

def is_prime(x):
    '''
    Checks if a valid input x is a prime number
    Evaluates in one line
    Returns True is x is prime
    Returns False is x is not prime
    x is of type int 
    '''
    return not bool(len([i for i 
                         in range(2,(x//2)+1) if x%i==0]))

prime_check(1373)


# In[ ]:



