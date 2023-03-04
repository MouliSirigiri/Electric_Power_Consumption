# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 11:20:02 2023

@author: mouli
"""
# importing library
import matplotlib.pyplot as plt
import pandas as pd
# import google link of the required data as url
url = 'https://drive.google.com/file/d/1haOwxP2Mo_WkIPlhwQngGbmd9h8vZTdO/view?usp=drivesdk'
# read the csv file of Electric power consumption as E_P_C from above link
E_P_C = pd.read_csv(
    "https://drive.google.com/uc?export=download&id="+url.split('/')[-2])
print(E_P_C)
E_P_C = E_P_C.drop(columns=['Series Name', 'Series Code',
                            'Country Code'])
# dropna function helps delete the rows of NULL values
E_P_C = E_P_C.dropna()
# Use rename() to change the name of column Country Name as Country
E_P_C = E_P_C.rename(columns={'Country Name': 'Country'})
print(E_P_C)

# line plot
# creating data on which line plot will be plot
year = ['2001', '2002', '2003', '2004', '2005', '2006', '2007',
        '2008', '2009', '2010', '2011', '2012', '2013', '2014']
# setting figure size by using figure() function
plt.figure(figsize=(10, 8))
# making the line plot of different countries on the taken data
plt.plot(year, E_P_C.iloc[0, 1:15], label='Australia')
plt.plot(year, E_P_C.iloc[1, 1:15], label='Canada')
plt.plot(year, E_P_C.iloc[2, 1:15], label='China')
plt.plot(year, E_P_C.iloc[3, 1:15], label='India')
plt.plot(year, E_P_C.iloc[4, 1:15], label='Russia')
plt.plot(year, E_P_C.iloc[5, 1:15], label='UAE')
plt.plot(year, E_P_C.iloc[6, 1:15], label='USA')
plt.plot(year, E_P_C.iloc[7, 1:15], label='UK')
# giving labels to x-axis and y-axis
plt.xlabel('Year')
plt.ylabel('Electric Power Consumption(kWh per capita)')
# giving title to graph
plt.title('Electric Power Consumption(kWh per capita)')
# creating legend will  helps to describe all the elements in the graph
plt.legend()
plt.show()

# bar graph of year 2008
# creating data on which bar chart will be plot
x = E_P_C['Country']
y = E_P_C['2008 [YR2008]']
# setting figure size by using figure() function
plt.figure(figsize=(16, 6))
# function to add value labels


def addlabels(x, y):
    """ giving the values on the bar """
    for i in range(len(x)):
        plt.text(i, y[i], y[i], ha='center')


# making the bar chart on the taken data
plt.bar(x, y, label='Electric Power Consumption(kWh per capita)', 
        color='darkgreen')
# calling the function to add value labels
addlabels(x, y)
plt.xlabel('Country')
plt.ylabel('Electric Power Consumption(kWh per capita)')
# rotating the xlable to 45 degrees
plt.xticks(rotation=45)
plt.title('Electric Power Consumption(kWh per capita) in year 2008')
plt.legend()
plt.show()

# pie chart of year 2001
# setting figure size by using figure() function
plt.figure(figsize=(8, 5))
# making the pie chart on the taken data
plt.pie(E_P_C['2001 [YR2001]'], labels=E_P_C['Country'],
        autopct='%1.2f%%', pctdistance=1.1, labeldistance=1.25)
plt.title('pie chart of Electric Power Consumption(kWh per capita) in year 2001')
plt.show()

# pie chart of year 2014
# setting figure size by using figure() function
plt.figure(figsize=(8, 5))
# making the pie chart on the taken data
plt.pie(E_P_C['2014 [YR2014]'], labels=E_P_C['Country'],
        autopct='%1.2f%%',  pctdistance=1.1, labeldistance=1.25)
plt.title('pie chart of Electric Power Consumption(kWh per capita) in year 2014')
plt.show()
