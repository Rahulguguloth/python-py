#!/usr/bin/env python
# coding: utf-8

# # Numpy
# Numpy is a linear algebra in python and it is the holy grail and the main building blockof data science using python

# In[1]:


pip install numpy


# In[3]:


import numpy as np
arr1 = np.array([1,2,3,4,5])
arr1


# In[4]:


arr1.size


# In[6]:


my_mat=([1,2,3,4],[5,6,7,8],[9,2,5,7])
my_mat


# In[7]:


b=np.array(my_mat)
b


# In[8]:


import numpy as np
# integer types
int8_arr = np.array([1,2,3],dtype=np.int8)
int16_arr = np.array([1000,-2000,3000],dtype=np.int16)
int32_arr = np.array([-10000,20000,30000],dtype=np.int32)
int64_arr = np.array([10000000,20000000],dtype=np.int64)


# In[9]:


# float type
float16_arr=np.array([1.1,-2.2,3.3],dtype=np.float16)
float32_arr = np.array([1.112345,-2.212345,3.321123],dtype=np.float32)
float16_arr = np.array([1.5434534541,-2.2123456789,.31234234567],dtype=np.float16)


# In[16]:


# complex type
complex64_arr = np.array([1-2j, 3+4j], dtype=np.complex64)
complex128_arr = np.array([1-2j, 3+4j], dtype=np.complex128)


# In[17]:


#boolean type
bool_arr=np.array([True,False,True],dtype=bool)
print("bool:",bool_arr,bool_arr.dtype)


# # string

# In[19]:


#string type
string_arr=np.array(["apple","banana","cherry"],dtype='<U10')


# In[20]:


#object type(mixed data types)
object_arr=np.array([1,"two",3.0,True],dtype=object)


# In[ ]:




