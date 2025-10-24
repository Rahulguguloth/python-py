#!/usr/bin/env python
# coding: utf-8

# # part 1

# In[1]:


import pandas as pd
import numpy as np

dataset_path = 'sales.csv'  

# Load dataset
df = pd.read_csv(dataset_path)


# In[2]:


# Display first and last 5 rows
print("First 5 rows:")
display(df.head())
print("\nLast 5 rows:")
display(df.tail())


# In[9]:


df.info()


# In[10]:


df.shape


# In[11]:


df.columns


# In[12]:


df.describe()


# In[14]:


# total + avg sales grouped by month (Jan to Apr included)
df.groupby('Month')['Sales'].agg(['sum', 'mean'])


# In[15]:


df['Sales'].sum()


# # part 2

# In[16]:


# total sales per city per month
df.groupby(['City', 'Month'])['Sales'].sum()


# In[17]:


# average monthly sales per city
df.groupby('City')['Sales'].mean()


# In[18]:


# city with highest average sales
df.groupby('City')['Sales'].mean().idxmax()


# In[19]:


# city with lowest total sales
df.groupby('City')['Sales'].sum().idxmin()


# In[20]:


# each city's total across months
city_total = df.groupby('City')['Sales'].sum()
city_total


# In[23]:


city_total.nlargest(3)


# In[24]:


# top 5 stores by total sales
df.groupby('City')['Sales'].sum().nlargest(5)


# In[25]:


# bottom 5 stores by total sales
df.groupby('City')['Sales'].sum().nsmallest(5)


# # part 3

# In[26]:


# store with highest sales in March
df[df['Month']==3].groupby('City')['Sales'].sum().idxmax()


# In[27]:


# store with lowest sales in April
df[df['Month']==4].groupby('City')['Sales'].sum().idxmin()


# In[28]:


# number of stores per city where avg monthly sales > 15
df.groupby('City')['Sales'].mean() > 15


# In[29]:


# stores in California having any monthly sales > 20
df[(df['Purchase Address'].str.contains(', CA')) & (df['Sales'] > 20)]


# # part 4

# In[30]:


# mean, max, min sales per city
df.groupby('City')['Sales'].agg(['mean','max','min'])


# In[31]:


# city with highest avg March sales
df[df['Month']==3].groupby('City')['Sales'].mean().idxmax()


# In[32]:


# overall avg sales per city
df.groupby('City')['Sales'].mean()


# In[33]:


# month with highest overall sales
df.groupby('Month')['Sales'].sum().idxmax()


# In[34]:


# each city's best month
df.groupby(['City','Month'])['Sales'].sum().groupby('City').idxmax()


# In[35]:


# add average sales column per city
avg_city = df.groupby('City')['Sales'].mean()
avg_city


# In[36]:


# sorted by avg sales (desc)
avg_city.sort_values(ascending=False)


# # part 5

# In[40]:


# total sales by city (bar chart)
import matplotlib.pyplot as plt

df.groupby('City')['Sales'].sum().plot(kind='bar')
plt.title("Total Sales by City")
plt.show()


# In[41]:


# average monthly sales (line chart)
df.groupby('Month')['Sales'].mean().plot(kind='line')
plt.title("Average Monthly Sales")
plt.show()


# In[42]:


df.groupby('City')['Sales'].sum().plot(kind='pie', autopct='%1.1f%%')
plt.title("City Share of Total Sales")
plt.ylabel("")  
plt.show()


# In[43]:


# top 10 stores total sales (horizontal bar chart)
df.groupby('City')['Sales'].sum().nlargest(10).plot(kind='barh')
plt.title("Top 10 Stores by Total Sales")
plt.show()


# In[44]:


# boxplot of monthly sales distribution by city
df.boxplot(column='Sales', by='City', vert=False)
plt.title("Sales Distribution by City")
plt.suptitle("")  
plt.show()


# In[ ]:




