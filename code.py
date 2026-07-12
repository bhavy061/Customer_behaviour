#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas  as pd
df = pd.read_csv('customer_shopping_behavior.csv')


# In[2]:


df.head(5)


# In[3]:


df.info()


# In[4]:


df.describe()


# In[5]:


df.isnull().sum()


# In[6]:


df['Review Rating'] = df.groupby('Category')['Review Rating'].transform(lambda x: x.fillna(x.median()))


# In[7]:


df.isnull().sum()


# In[8]:


df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(' ','_')
df = df.rename(columns={'purchase_amount_(usd)': 'purchase_amount'})


# In[9]:


df.columns


# In[10]:


# create a column age_group
labels = ['Young Adult','Adult','Middle_aged','Senior']
df['age_group'] = pd.qcut(df['age'],q=4,labels=labels)


# In[11]:


df[['age','age_group']].head(10)


# In[13]:


# create purchase_frequency_days

frequency_mapping = {
    'Fortnightly' : 14,
    'Weekly' : 7,
    'Monthly' : 30,
    'Quarterly' : 90,
    'Bi-Weekly' : 14,
    'Annually' : 365,
    'Every 3 Months' : 90
}
df['purchase_frequency_days'] = df['frequency_of_purchases'].map(frequency_mapping)
 


# In[14]:


df[['purchase_frequency_days','frequency_of_purchases']].head(10)


# In[18]:


df[['discount_applied','promo_code_used']].head(10)


# In[19]:


(df['discount_applied'] == df['promo_code_used']).all()


# In[20]:


df = df.drop('promo_code_used',axis=1)


# In[21]:


df.columns


# In[22]:


pip install psycopg2-binary sqlalchemy


# In[25]:


from sqlalchemy import create_engine
username = "postgres"
password = "bhavya"
host = "localhost"
port = "5432"
database = "customer_behaviour"

engine = create_engine(f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}")

table_name = "customer"
df.to_sql(table_name,engine,if_exists="replace",index=False)
print(f"Data successfully loaded into table '{table_name}' in database '{database}'")


# In[ ]:




