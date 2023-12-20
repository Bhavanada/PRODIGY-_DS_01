#!/usr/bin/env python
# coding: utf-8

# In[1]:


#WORLD BANK TASK 01
import pandas as pd
import matplotlib.pyplot as plt

# URL for the World Bank dataset containing total population data
#url = "http://api.worldbank.org/v2/en/indicator/SP.POP.TOTL?downloadformat=csv"

# Read the dataset from the provided URL skipping the header rows
data = pd.read_csv("C:\\Users\\compaq\\Desktop\\World_Bank.csv")

# Displaying the available columns to identify the column containing population data
print(data.columns)

# Assuming '2019' column contains total population data for the year 2019
population_data = data['Unnamed: 66'].dropna()  # Extracting population data and dropping NaN values

# Plotting a histogram for total population distribution
plt.figure(figsize=(8, 6))
plt.hist(population_data, bins=50, color='skyblue', edgecolor='black')
plt.xlabel('Total Population')
plt.ylabel('Frequency')
plt.title('Distribution of Total Population (2019)')
plt.grid(True)
plt.show()


# In[ ]:




