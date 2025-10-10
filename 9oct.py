#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install mysql-connector-python


# In[4]:


import mysql.connector
import pandas as pd
mypd = mysql.connector.connect(
    host="localhost",
    user="root",
    password="R@hul123",
    database="rahul"
)
print("hi")


# In[ ]:




