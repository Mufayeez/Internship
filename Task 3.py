#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
import pandas as pd
from bs4 import BeautifulSoup


# In[3]:


url = 'https://en.wikipedia.org/wiki/List_of_Indian_states_and_union_territories_by_GDP_per_capita'


# In[4]:


response =requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
soup


# In[5]:


table = soup.find('table', {'class' : 'wikitable sortable'})
table


# In[6]:


state_names = []
per_capita_rs = []
per_capita_usd = []

rows = table.find_all('tr')
for row in rows[1:]:
    cells = row.find_all('td')
    if len(cells) > -4:
        state_name = cells[1].text.strip()
        per_capita_text_rs = cells[2].text.strip()
        per_capita_text_usd = cells[3].text.strip()
        per_capita_split_rs = per_capita_text_rs.split('IN₹')
        per_capita_split_usd = per_capita_text_usd.split('US$')
        
        per_capita_rs.append(per_capita_split_rs[0])
        per_capita_usd.append(per_capita_split_usd[0].replace(')',''))
        state_names.append(state_name)


# In[8]:


data = {'State': state_names, 'Per Capita (Rupees)' : per_capita_rs, 'Per Capita (USD)' : per_capita_usd}
df = pd.DataFrame(data)
df


# In[9]:


df.dtypes


# In[10]:


df['Per Capita Income (Rupees)'] = df['Per Capita (Rupees)'].str[1:]


# In[11]:


df.head()


# In[12]:


df['Per Capita Income (Rupees)'] = df['Per Capita Income (Rupees)'].str.replace(',','')


# In[13]:


df.head()


# In[14]:


import geopandas as gpd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[15]:


shp_gdf = gpd.read_file('C:/Users/mufay/OneDrive/Documents/India States/India_State_Boundary.shp')


# In[16]:


shp_gdf.head()


# In[17]:


merged = shp_gdf.set_index('Name').join(df.set_index('State'), how = 'right')
merged


# In[19]:


fig, ax = plt.subplots(1, figsize = (12,12))
ax.axis('off')
ax.set_title('Per Capita Income of Indians as Per State', fontdict={'fontsize':'15', 'fontweight' : '3'})
fig = merged.plot(column = 'Per Capita Income (Rupees)', cmap = 'RdYlGn', linewidth = 0.5, ax=ax, edgecolor = '0.2', legend = True)


# In[20]:


min_value = merged['Per Capita Income (Rupees)'].min()
max_value = merged['Per Capita Income (Rupees)'].max()


# In[21]:


fig = px.choropleth(
    merged,
    geojson=merged.geometry,
    locations=merged.index,
    color='Per Capita Income (Rupees)',
    color_continuous_scale='Blues',
    range_color=(df['Per Capita Income'].min(), df['Per Capita Income'].max()),
    scope='asia',


# In[22]:


merged.plot(column='Per Capita Income (Rupees)', cmap='Blues', linewidth=0.8, ax=ax, edgecolor='0.8')


# In[23]:


sm = plt.cm.ScalarMappable(cmap='Blues', norm=plt.Normalize(vmin=min_value, vmax=max_value))
sm.set_array([])
fig.colorbar(sm)


# In[26]:


plt.title('Per Capita Income in Indian States')
plt.xlabel('Longitude')
plt.ylabel('Latitude')


# In[27]:


plt.show()


# In[ ]:





# In[25]:


plt.show()


# In[ ]:





# In[ ]:





# In[1]:





# In[ ]:




