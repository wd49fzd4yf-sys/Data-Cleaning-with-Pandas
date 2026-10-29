#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[ ]:


flights_data = pd.read_csv('flights.csv')
flights_data.head(10)
weather_data_pd = pd.read_csv('weather.csv')
weather_data_np = weather_data_pd.to_numpy()
#use flights_data


# In[ ]:


flights_data.columns


# In[ ]:


# Question 1: filter on origin AND dest, then count rows
q_1 = len(flights_data[(flights_data['origin'] == 'JFK') & (flights_data['dest'] == 'SLC')])
print(q_1)


# In[ ]:


# Question 2: filter to SLC, count distinct airlines, should be int
q_2 = flights_data[flights_data['dest'] == 'SLC']['carrier'].nunique()
print(q_2)


# In[ ]:


# Question 3: What is the average arrival delay for flights to RDU? float
q_3 = flights_data[flights_data['dest'] == 'RDU']['arr_delay'].mean()
print(q_3)


# In[ ]:


# Question 4: What proportion of flights to SEA come from the two NYC airports? float
sea = flights_data[flights_data['dest'] == 'SEA']
q_4 = sea['origin'].isin(['LGA', 'JFK']).mean()
print(q_4)


# In[ ]:


# Question 5: Which date has the largest average departure delay? Pd slice with date and float. 
# Please make a date column. Preferred format is 2013/1/1 (y/m/d)
flights_data['date'] = (flights_data['year'].astype(str) + '/' +
                        flights_data['month'].astype(str) + '/' +
                        flights_data['day'].astype(str))
q_5 = (flights_data.groupby('date')['dep_delay'].mean()
       .reset_index()
       .sort_values('dep_delay', ascending=False)
       .head(1))
print(q_5)


# In[ ]:


# Question 6: same as Q5 but with arr_delay
q_6 = (flights_data.groupby('date')['arr_delay'].mean()
       .reset_index()
       .sort_values('arr_delay', ascending=False)
       .head(1))
print(q_6)


# In[ ]:


# Question 7: Which flight departing LGA or JFK in 2013 flew the fastest? pd slice with tailnumber
nyc = flights_data[(flights_data['origin'].isin(['LGA', 'JFK'])) &
                    (flights_data['year'] == 2013)].copy()
nyc['speed'] = nyc['distance'] / nyc['air_time']
q_7 = (nyc.dropna(subset=['speed'])
       .sort_values('speed', ascending=False)[['tailnum', 'speed']]
       .head(1))
print(q_7)


# In[ ]:


# Question 8: replace all nans in the weather pd dataframe with 0s. Pd with no nans
q_8 = weather_data_pd.fillna(0)
print(q_8)


# In[ ]:


# Numpy Data Filtering/Sorting Question Answering
#Use weather_data_np
month_col = weather_data_pd.columns.get_loc('month')
humid_col = weather_data_pd.columns.get_loc('humid')
# Keep only February rows
feb_mask = weather_data_np[:, month_col] == 2
feb_humid = weather_data_np[feb_mask, humid_col].astype(float)


# In[ ]:


# Question 9: How many observations were made in February? Int
q_9 = int(feb_mask.sum())
print(q_9)


# In[ ]:


# Question 10: What was the mean for humidity in February? Float
q_10 = np.nanmean(feb_humid)
print(q_10)


# In[ ]:


# Question 11 What was the std for humidity in February? Float
q_11 = np.nanstd(feb_humid)
print(q_11)


# In[ ]:




