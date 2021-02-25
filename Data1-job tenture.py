#!/usr/bin/env python
# coding: utf-8

# In[131]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[132]:


data=pd.read_csv(r"G:/Sem_4/Milestone 1/14100050-eng/14100050.csv")


# In[133]:


data


# In[134]:


data.head()


# In[135]:


data.shape


# In[136]:


data.index


# In[137]:


data.columns


# In[138]:


data.dtypes


# In[139]:


data.nunique()


# In[140]:


data.count()


# In[141]:


data['Age group'].unique


# In[142]:


data['REF_DATE'].unique


# In[143]:


data['GEO'].unique


# In[144]:


data['DGUID'].unique


# In[145]:


data['Type of work'].unique


# In[146]:


data['Sex'].unique


# In[147]:


data['UOM'].unique


# In[148]:


data['Age group'].value_counts


# In[149]:


data.info()


# In[150]:


data.head(2)


# In[151]:


data['DGUID'].nunique()


# In[152]:


data['DGUID'].unique()


# In[153]:


data['Age group'].nunique()


# In[154]:


data['Age group'].unique()


# In[155]:


#value_counts()
data.DGUID.value_counts()


# In[156]:


#value_counts()
data.Sex.value_counts()


# In[157]:


#value_counts()
data.SCALAR_ID.value_counts()


# In[158]:


#value_counts()
data.VECTOR.value_counts()


# In[159]:


#value_counts()
data.VALUE.value_counts()


# In[160]:


data.head(2)


# In[161]:


data[data['Sex'] == 'Both sexes']


# In[162]:


#find out all the null values in data
data.isnull()


# In[163]:


data.isnull().sum()


# In[164]:


data.notnull().sum()


# In[165]:


data.head(2)


# In[166]:


data.rename(columns = {'REF_DATE' : 'DATE'} , inplace=True)
data.head()


# In[167]:


data.UOM_ID.mean()


# In[168]:


data.UOM_ID.std()


# In[169]:


data['UOM_ID'].var()


# In[170]:


data['Age group'].value_counts()


# In[171]:


data[data["UOM_ID"] == 220]


# In[172]:


data.head(5)


# In[187]:


data['VECTOR'].value_counts()[0:5]


# In[188]:


plt.figure(figsize=(8, 5))
plt.bar(list(data['VECTOR'].value_counts()[0:5].keys()), list(data['VECTOR'].value_counts()[0:5]), color="g")
plt.show()


# In[189]:


data['Age group'].value_counts()[0:5]


# In[196]:


plt.figure(figsize=(8, 5))
plt.bar(list(data['Age group'].value_counts()[0:5].keys()), list(data['Age group'].value_counts()[0:5]), color="b")
plt.show()


# In[193]:


data['VALUE'].value_counts()


# In[195]:


plt.figure(figsize=(8, 5))
plt.bar(list(data['VALUE'].value_counts().keys()), list(data['VALUE'].value_counts()), color="g")
plt.show()


# In[199]:


#making a pie chart
plt.figure(figsize=(7,10))
plt.pie(list(data['Age group'].value_counts()[0:500]), labels=list(data['Age group'].value_counts()[0:500].keys()),autopct='%0.1f%%')
plt.show()


# In[208]:


#making a pie chart
plt.figure(figsize=(7,10))
plt.pie(list(data['Sex'].value_counts()), labels=list(data['Sex'].value_counts().keys()),autopct='%0.1f%%')
plt.show()


# In[207]:


#making a pie chart
plt.figure(figsize=(7,10))
plt.pie(list(data['UOM_ID'].value_counts()), labels=list(data['UOM_ID'].value_counts().keys()),autopct='%0.1f%%')
plt.show()

