#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


data = pd.read_csv('F://Profession//Interships//Newbieron technologies//Task 7//IDSCountry.csv')


# In[3]:


data.head()


# In[4]:


data.info()


# In[5]:


data.isnull().sum()


# In[6]:


data.describe()


# In[7]:


data.shape


# In[8]:


data1 = pd.read_csv('F://Profession//Interships//Newbieron technologies//Task 7//IDSCountry-Series.csv')


# In[9]:


data1.head()


# In[10]:


data1 = data1.drop('Unnamed: 3', axis = 1)


# In[11]:


data1.head()


# In[13]:


data1.info()


# In[14]:


data1.isnull().sum()


# In[15]:


data1.shape


# In[16]:


data2 = pd.read_csv('F://Profession//Interships//Newbieron technologies//Task 7//IDSData.csv')


# In[17]:


data2.head()


# In[18]:


data2 = data2.drop('Unnamed: 59', axis=1)


# In[19]:


data2.head()


# In[20]:


data2.shape


# In[22]:


data2.info()


# In[23]:


data2.isnull().sum()


# In[24]:


data2 = data2.fillna(0)


# In[25]:


data2.head()


# In[26]:


data2.isnull().sum()


# In[27]:


data2.describe()


# In[28]:


data2.to_csv('Final_IDS.csv')


# In[ ]:





# In[ ]:





# In[ ]:




