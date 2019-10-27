
# coding: utf-8

# ## Various ways of importing data into python with pandas.

# ### Delimited files ( csv ,tsv)

# In[1]:

# importing all the packages at first, for now we only need pandas package
import pandas as pd

# just like that ( you can pass delimiter argument if its tsv)
data=pd.read_csv('insurance.csv')
data.head()


# ### from relational databases (SQL)

# In[6]:

import pymysql as sql

#connecting to database on machine it could be from remote machine too
conn=sql.connect(host='localhost',user='root',password='',db="capstone")

# this step is necessary before querying database
c=conn.cursor()
# execute the command 
c.execute('select * from lab_profile;')
# fetching into rows its spits list
all_rows=c.fetchall()

#creating a dataframe with it
df=pd.DataFrame(list(all_rows),columns=["id","name","location","password"])
df.head()


# ### scraping data from websites 

# In[41]:

import requests,bs4

# sometimes we need customization before collecting data from website 
url='https://www.amazon.in/Samsung-Galaxy-Storage-Additional-Exchange/dp/B07KXBMYCW/ref=br_msw_pdt-3?_encoding=UTF8&smid=A14CZOWI0VEHLG&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_s=&pf_rd_r=1KZ2D3KPDEM30DF6XTCB&pf_rd_t=36701&pf_rd_p=cc9b62a5-2189-486a-89b4-4eda80243fbe&pf_rd_i=desktop'
soup = bs4.BeautifulSoup(requests.get(url).text,"lxml")

div=soup.select("a") # this step will take time and here we customize depending upon webssite

data=pd.DataFrame(div,columns=['links'])
data.head()


# ### Getting from API

# In[49]:

import json
import pprint

# api are different but what is common is they generally spit out response on JSON format which is
# same as dictionary so we can use simple function to convert into dataframe
r=requests.get('https://www.metaweather.com/api/location/search/?query=san').text

# some api needs key and specific fromat before getting data you need to go through all the process
rdict=json.loads(r)
apidata=pd.DataFrame.from_dict(rdict,orient='columns')
apidata.head()


# ### from PDF documents

# In[64]:

import PyPDF2 as pdf

#open up like a file 
pdoc=open('bank.pdf','rb')

# that PdfFileReader  method for converting that opened file into some supported format
pdfreader=pdf.PdfFileReader(pdoc)

# get num of pages to caution out before passing the page it doesn't exist at all
print(pdfreader.getNumPages())


page=pdfreader.getPage(2)

pdfdata=page.extractText()
# IDK from here onwards how to convert that string into dataframe. You can go do some string operations.
print(pdfdata)
pdoc.close()

