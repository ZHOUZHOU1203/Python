#!/usr/bin/env python
# coding: utf-8

# In[7]:


#leggi:x,y,z
def min(x,y,z):
    if(x<y):
        if(x<z):
            print(x)
        else:        #x>=z
            print(z)
    else:#x>=y
        if(y<z):
            print(y)
        else:           #y>=z
            print(z)
                    
                
            
        
    
          


# In[8]:


min(5,15,20)


# In[10]:


min(10,100,1)


# In[11]:


min(2000000000000000000000000000000000000000,28,28327272)


# In[13]:


min(1.11111111,2.1,3.4)


# In[14]:


print("Hello World!")


# In[15]:


print("Hello again!")


# In[16]:


print(f"Let's talk about {my_name}.") 


# In[ ]:




