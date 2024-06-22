# Step 1: Import Library

import pandas as pd
import numpy as np
import seaborn as sns
import os
import datetime
import matplotlib.pyplot as plt

# Step 2: Read the dataset

energy_data = pd.read_csv("C:/Aman/DPC/Self Projects/Hourly energy/AEP_hourly.csv")

'''print(energy_data.head(6))

print(energy_data.describe())
energy_data.info() '''


# Step 3: Separate Date and Time

energy_data["new_date"] = pd.to_datetime(energy_data["Datetime"]).dt.date

energy_data["new_time"] = pd.to_datetime(energy_data["Datetime"]).dt.time

energy_data["Month"] = pd.to_datetime(energy_data["Datetime"]).dt.month


energy_data["Year"] = pd.to_datetime(energy_data["Datetime"]).dt.year

#print(energy_data.head(5))

#print(energy_data["Year"].unique())

#print(energy_data["Year"].nunique())


'''
# maximum energy consumed in year 2004 in MW

print(energy_data[energy_data["Year"] == 2004]["AEP_MW"].max())

# minimum energy consumed in year 2004 in MW

print(energy_data[energy_data["Year"] == 2004]["AEP_MW"].min())

# average energy consumed in year 2004 in MW

print(energy_data[energy_data["Year"] == 2004]["AEP_MW"].mean())
'''

# Energy Distribution
'''
sns.distplot(energy_data["AEP_MW"])
plt.show()
'''

# Relationship between the year and MW
# Energy consumption throughout the year
'''
sns.lineplot(x = energy_data["Year"], y = energy_data["AEP_MW"], data = energy_data)
plt.show()
'''
# Graph for 2007
'''
energy_data[energy_data["Year"] == 2007]["AEP_MW"].plot()
plt.show()
'''

# Regression and kde (Kernel density estimate) plot
'''
sns.jointplot(x = energy_data["Year"], y = energy_data["AEP_MW"], data= energy_data, kind = "kde")
plt.show()

sns.lineplot(x = energy_data["new_time"], y = energy_data["AEP_MW"], data= energy_data)
plt.show()
'''
# Extracting data on date range

#print(energy_data.head(4))

print(energy_data["new_date"].describe())

print(energy_data.set_index(energy_data["new_date"]).head(2))

#energy_data[(energy_data["new_date"] > "2005-10-01") & (energy_data["new_date"] <= "2007-10-01")]

print(energy_data.loc["2005-10-01" : "2007-10-01"])