#!/usr/bin/env python
# coding: utf-8

# In[9]:


pip install beautifulsoup4


# In[10]:


import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
import pandas as pd
import bson
from bson.raw_bson import RawBSONDocument

db_client = MongoClient()
my_db = db_client.cursos
my_posts = my_db.posts
    
def find_2nd(string, substring):
    return string.find(substring, string.find(substring) + 1)
def find_1st(string, substring):
    return string.find(substring, string.find(substring))

response = requests.get("https://olympics.com/tokyo-2020/es/noticias/")
soup = BeautifulSoup(response.content, "lxml")

Titulos=[]
Contenido=[]


titulos = soup.find_all("span", class_="tk-card__topic")
contenido=soup.find_all("span", class_="tk-card__titlelink")

extracted = []
  
for element in titulos:
    #print(element)
    element=str(element)
    limpio=str(element[find_1st(element, '>')+1:find_2nd(element,'<')])
    #print (limpio)
    Titulos.append(limpio.strip())

for element in contenido:
    #print(element)
    element=str(element)
    limpio=str(element[find_1st(element, '>')+1:find_2nd(element,'<')])
    #print (limpio)
    Contenido.append(limpio.strip())

print(Titulos)
print(Contenido)

from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient('mongodb+srv://admin:admin@cluster0.zm8dw.mongodb.net/test')
db=client.admin
# Issue the serverStatus command and print the results

serverStatusResult=db.command("serverStatus")
pprint(serverStatusResult)


# In[ ]:




