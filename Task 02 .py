#!/usr/bin/env python
# coding: utf-8

# In[68]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[69]:


url = 'https://www.ndtv.com/coronavirus/india-covid-19-tracker'
response = requests.get(url)
html_content = response.content


# In[70]:


soup = BeautifulSoup(html_content, 'html.parser')


# In[83]:


table = soup.find("table table-striped table-bordered")

if table is not None:
    rows = table.find_all("tr")

    data = []
    for row in rows:
        cells = row.find_all("td")
        if len(cells) == 5:
            row_data = [cell.text.strip() for cell in cells]
            data.append(row_data)

    df = pd.DataFrame(data, columns=["#", "State/UT", "Confirmed Cases", "Active Cases", "Cured/Discharged", "Death"])
    df = df.iloc[1:]  # Remove the header row
    df.reset_index(drop=True, inplace=True)


# In[84]:


numeric_cols = ["#", "Confirmed Cases", "Active Cases", "Cured/Discharged", "Death"]
df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors="coerce")


# In[ ]:





# In[ ]:




