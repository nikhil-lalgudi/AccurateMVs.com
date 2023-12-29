#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import requests
from bs4 import BeautifulSoup


url = "https://fbref.com/en/comps/Big5/2022-2023/stats/players/2022-2023-Big-5-European-Leagues-Stats"
res = requests.get(url)
soup = BeautifulSoup(res.content, 'html.parser')


table = soup.find_all('table')[0]


df_list = pd.read_html(str(table), header=0)
df = pd.concat(df_list)
df = df.iloc[:,[1,2,3,4,5,6,9,11]]


df.columns = ["Player", "Nation", "Pos", "Squad", "Comp", "Age", "Starts", "90s"]


df.to_excel('soccer_data.xlsx', index=False)


# In[ ]:




