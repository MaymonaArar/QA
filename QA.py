#!/usr/bin/env python
# coding: utf-8

# # Magic number test

# In[32]:


test = False
with open('Magic number code.txt') as f:
    lines = f.readlines()
    for line in lines:
        for char in line:
            if char.isdigit():
                test = True 
if test :
    print("code have a magic number :( ")
if test==False  :
    print("code not have a magic number :) ")


# # Unreachable code test

# In[34]:


numReturn = False 
newWord=0
with open('Unreachable code.txt','r') as f:
    for line in f:
        for word in line.split():
            if word=='return':
                numReturn=True
            if numReturn and word:
                newWord=newWord+1
                

if newWord > 2:
    print("Unreachable code") 
    
else :
    print("Not unreachable code")
    


# In[ ]:





# In[ ]:




