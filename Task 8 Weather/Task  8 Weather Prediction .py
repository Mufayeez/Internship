#!/usr/bin/env python
# coding: utf-8

# In[36]:


# Importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
import plotly.express as px


# In[37]:


data = pd.read_csv('F://Profession//Interships//Newbieron technologies//Task 8//Raw data//weather.csv')


# In[38]:


data.head()


# In[39]:


data.info()


# In[40]:


data.shape


# In[41]:


data.isnull().sum()


# In[42]:


data.hist(bins=50, figsize=(15,15))


# In[43]:


data.plot(kind='scatter', x='MinTemp', y='MaxTemp', figsize=(10,7))
plt.title('Scatter Plot')
plt.xlabel('MinTemp')
plt.ylabel('MaxTemp')


# In[44]:


plt.figure(figsize=(10,7))
plt.title('Weather Prediction')
sns.histplot(x='Wind',hue='weather',data=data, )
plt.show()


# In[45]:


data1=data[['Rainfall','MaxTemp','MinTemp','Wind']]
weather1 = data[['Rainfall','MaxTemp','MinTemp','Wind', 'weather']]
figure = px.sunburst(weather1,path=['weather','Rainfall'],values='Wind',width=1000,height=1000)
figure.show()


# In[47]:


X = data[['Rainfall','MaxTemp','MinTemp','Wind']]
Y = data['weather']


# In[49]:


from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.30, random_state=42)


# In[61]:


data['weather'].value_counts()


# In[66]:


KNN = KNeighborsClassifier(n_neighbors=1)
KNN.fit(X,Y)


# In[ ]:


KNN.score(X,Y)


# In[ ]:


y_pred = KNN.predict(X_test)
y_pred


# In[ ]:


from sklearn.metrics import classification_report
print(classification_report(y_pred,Y_test))

