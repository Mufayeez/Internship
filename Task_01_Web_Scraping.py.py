#!/usr/bin/env python
# coding: utf-8

# In[5]:


import requests
from bs4 import BeautifulSoup
import urllib
import os

def scrape_google_images(person_name, num_images):
    query = person_name.replace(' ', '+')
    url = f"https://www.google.com/search?q={query}&tbm=isch"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    images = soup.find_all('img')
    count = 0
    if not os.path.exists(person_name):
        os.makedirs(person_name)
    for image in images:
        if count == num_images:
            break
        try:
            image_url = image['src']
            if image_url.startswith('http'):
                urllib.request.urlretrieve(image_url, f"{person_name}/{person_name}_{count}.jpg")
                count += 1
                print(f"Downloaded image {count} of {num_images}")
        except Exception as e:
            print(f"Error downloading image {count + 1}: {str(e)}")

person_name = input("Enter the name of the person: ")
num_images = 50

scrape_google_images(person_name, num_images)


# In[ ]:




