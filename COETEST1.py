#!/usr/bin/env python
# coding: utf-8

# # ASSINGMENT 1

# In[32]:


#Load data sets
import pandas as pd
ud=pd.read_csv("Uber_Drives_2016.csv")
ud.head()


# #Display the number of rows and columns.

# In[12]:


#
print(ud.shape)


# In[19]:


# showing all column names
ud.columns


# In[20]:


#data types of each column
ud.dtypes


# In[21]:


#  unique values in CATEGORY column
ud['CATEGORY*'].unique()


# In[23]:


#  null values in PURPOSE column
ud['PURPOSE*'].isnull().sum()


# In[25]:


# renaming all columns to uppercase & removing *
ud.columns = ud.columns.str.replace('*', '', regex=False).str.upper()
ud.columns


# # ASSINGMENT 2

# In[26]:


# filte  rides category is Business
ud[ud['CATEGORY'] == 'Business']


# In[27]:


# showing top 5 longest trips based on miles
ud.sort_values(by='MILES', ascending=False).head(5)


# In[29]:


# null values in purpose column
ud['PURPOSE'] = ud['PURPOSE'].fillna("Not Specified")
ud['PURPOSE'].isnull().sum()


# In[43]:


#Would you like me to show how to convert that TRIP_DURATION into hours or minutes for easier analysis
ud['TRIP_DURATION'] = ud['END_DATE'] - ud['START_DATE']
ud[['START_DATE', 'END_DATE', 'TRIP_DURATION']].head()


# In[44]:


#just to view a small sample of your data and confirm that the TRIP_DURATION calculation worked correctly
ud[['START_DATE', 'END_DATE', 'TRIP_DURATION']].head()


# In[45]:


#show how to sort by multiple columns (e.g., by category and miles)
ud.sort_values(by='MILES', ascending=False)


# # ASSINGMENT 3

# In[46]:


# average miles per category
a_miles = ud.groupby('CATEGORY')['MILES'].mean()
a_miles


# In[47]:


# counting trips based on purpose
p_count = ud['PURPOSE'].value_counts()
p_count


# In[48]:


# finding top 3 most common start locations
t_start_loc = ud['START'].value_counts().head(3)
t_start_loc


# In[51]:


#that’s a Matplotlib bar chart command that visualizes the average miles per category.
import matplotlib.pyplot as plt

# bar chart of average miles
a_miles.plot(kind='bar')

plt.title("Average Miles by Category")
plt.xlabel("Category")
plt.ylabel("Average Miles")
plt.show()


# In[52]:


# pie chart of trip purposes
p_count.plot(kind='pie', autopct='%1.1f%%')

plt.title("Distribution of Trip Purposes")
plt.ylabel("")  
plt.show()


# In[ ]:




