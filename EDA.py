#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import numpy as np
import chart_studio.plotly as py
import cufflinks as cf
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

# Make Plotly work in your Jupyter Notebook
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)
# Use Plotly locally
cf.go_offline()


# In[2]:


df = pd.read_csv("E:/Ineuron Internship/Automated ML/Final/Datasets/diabetes-dataset.csv")
df.head()


# In[3]:


df.isnull().sum()


# In[4]:


df.corr()


# In[7]:


#Get Correlation between different variables
corr = df.corr(method='kendall')
plt.figure(figsize=(15,8))
sns.heatmap(corr, annot=True)
df.columns


# In[ ]:


sns.pairplot(data=df.corr())


# In[ ]:


sns.jointplot(data=df, x="Age",y='BloodPressure')


# In[ ]:


sns.jointplot(data=df, x="Age",y='Glucose')


# In[ ]:


sns.jointplot(data=df, x="Age",y='Insulin')


# In[ ]:


sns.jointplot(data=df, x="Age",y='DiabetesPedigreeFunction')


# In[ ]:


# Allows us to create graph objects for making more customized plots 
import plotly.graph_objects as go


# In[ ]:


# Create a scatter plot using flight data
fig = px.scatter(df,y='BloodPressure', x='Age', color = 'Outcome',
                   opacity=0.7, width=800, height=400)
fig


# In[ ]:


# Create a scatter plot using flight data
fig = px.scatter(df,y='Glucose', x='Age', color = 'Outcome',
                   opacity=0.7, width=800, height=400)
fig


# In[ ]:


# Create a scatter plot using flight data
fig = px.scatter(df,y='Insulin', x='Age', color = 'Outcome',
                   opacity=0.7, width=800, height=400)
fig


# In[ ]:


# Create a scatter plot using flight data
fig = px.scatter(df,y='DiabetesPedigreeFunction', x='Age', color = 'Outcome',
                   opacity=0.7, width=800, height=400)
fig


# In[ ]:




