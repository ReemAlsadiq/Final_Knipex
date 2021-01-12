#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from requests import exceptions
from bs4 import BeautifulSoup 
import pandas as pd


# In[2]:


df = pd.read_excel('/Users/apple/Desktop/Knipex.xlsx')
df


# In[3]:


def get_soup(url):  
    try:
        req = requests.get(url,verify=False)
        soup = BeautifulSoup(req.text)
        #print(soup)
        return soup
    except:
        pass


# In[4]:


df_soup = df['Product URL'].apply(lambda x: get_soup(x))


# In[5]:


df_soup


# In[6]:


def get_img(soup):
    try:
        img = soup.find('img',{'class': 'prod_zoom'}).get('src')
        #print(img)
        return img
    except:  
        pass


# In[7]:


df['Image2'] = df_soup.apply(lambda x: get_img(x))


# In[68]:


df.to_excel('/Users/apple/Desktop/Knipex_Scraped.xlsx')


# In[8]:


def get_table(soup):
    try:
        My_table = soup.find('table',{'id':'my-table'})
        #print(My_table)
        return My_table
    except:
        pass


# In[9]:


My_table_list = []
for s in df_soup:
    My_table = get_table(s)
    My_table_list.append(My_table)
#print(My_table_list)  


# In[10]:


def get_table_rows(soup):
    try:
        table_rows = My_table.findAll('tr')
        #print(table_rows)
        return table_rows
    except:
        return 


# In[11]:


My_table_rows_list = []
for tr in My_table:
    My_table_row = get_table_rows(s)
    My_table_rows_list.append(My_table_row)
#print(My_table_rows_list)  


# In[12]:


def get_th(soup):
    try:
        final_list = []
        intermediate_list = []
        for tr in My_table_row:
            for td in tr.findAll("th"):
                intermediate_list.append(td.findNext(text=True))
                final_list.append(intermediate_list)
                intermediate_list = []
        data = final_list    
        return data
    except:
        return


# In[13]:


My_table_th_list = []
for th in  My_table_row:
    My_table_th = get_th(th)
    My_table_th_list.append(My_table_th)
#print(My_table_th_list)   


# In[14]:


def get_td(soup):
    final_list1 = []
    intermediate_list1 = []
    for tr in My_table_row:
        for td in tr.findAll("td"):
            intermediate_list1.append(td.findNext(text=True))
            final_list1.append(intermediate_list1)
            intermediate_list1 = []
    data2 = final_list1 
    return data2


# In[15]:


My_table_td_list = []
for td in  My_table_row:
    My_table_td = get_td(td)
    My_table_td_list.append(My_table_td)
#print(My_table_td_list)


# In[67]:


def Extract(lst): 
    for list in lst:
        #print(list)
        return [item[0] for item in list]
    
y = Extract(My_table_th_list)
x = Extract(My_table_td_list)
print(y)
print(x)


# In[46]:


dictionary = dict(zip(y, x))
dictionary


# In[18]:


df2= pd.Series(dictionary)
df2 = pd.DataFrame(df2)
df2 = df2.transpose()
df2


# In[ ]:




