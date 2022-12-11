# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 05:50:55 2022

@author: HP
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def read_file(filename):
    data = pd.read_excel(filename)
    datatranspose= data.set_index('Country Name').transpose()
    return data, datatranspose
    

country_list1= ['China','United Kingdom','India','Cuba','Italy','Argentina']

country_list2= ['India','Pakistan','Saudi Arabia','Australia','Bangladesh','France']

def filter_bar_data(data):
    data=data[['Country Name','Indicator Name', '1995','1996','1997','1998','1999']]
    data = data [(data["Country Name"]=="China") | 
                 (data["Country Name"]=="United Kingdom") | 
                 (data["Country Name"]=="India") |
                 (data["Country Name"]=="Cuba") | 
                 (data["Country Name"]=="Italy") |
                 (data["Country Name"]=="Argentina")]
    return data

def filter_line_plot(data):
    data=data[['Country Name','Indicator Name','1990','2000','1994','2013','2019']]
    data =data [(data["Country Name"]=="India") | 
                (data["Country Name"]=="Pakistan") | 
                (data["Country Name"]=="Saudi Arabia") |
                (data["Country Name"]=="Australia") |
                (data["Country Name"]=="Bangladesh") | 
                (data["Country Name"]=="France")]
    return data
    
    
def barplot(data, label1, label2):
    plt.figure(figsize=(25,19))
    ax= plt.subplot(1,1,1)
    x = np.arange(6)
    width= 0.2

    bar1= ax.bar(x, data["1995"],width,label= 1995)
    bar2= ax.bar(x+width, data["1996"], width, label=1996)
    bar3= ax.bar(x+width*2, data["1997"], width, label=1997)
   
    
    ax.set_xlabel("Country Names", fontsize= 40)
    ax.set_ylabel(label1, fontsize= 40)
    ax.set_title(label2, fontsize=40)
    ax.set_xticks(x, country_list1, fontsize=30, rotation=90)
    ax.legend(fontsize=30)
             
    ax.bar_label(bar1, padding=2, rotation=90, fontsize= 18)
    ax.bar_label(bar2, padding=2, rotation=90, fontsize= 18)
    ax.bar_label(bar3, padding=2, rotation=90, fontsize= 18)
    
    plt.show()    
     
           
def line_plot(data,label1,label2):
    plt.figure(figsize=(25,10))
    dd = data.set_index('Country Name')
    tran = dd.transpose()
    tran = tran.drop(index=['Indicator Name'])
    for i in range(len(country_list2)):
        plt.plot(tran.index, tran[country_list2[i]], label=country_list2[i],linestyle='dashed',linewidth='3')
        
    plt.title(label2, size=18)
    plt.xlabel("Years", size=12)
    plt.ylabel(label1, size=12)
    plt.xticks(rotation=90)
    plt.legend(fontsize=6)
    plt.savefig("lineplot.png")
    plt.show()
             
Energy_data, Energy_data1 = read_file("C:/Users/HP/Documents/fname/Energy use.xls")
Energy_data = filter_bar_data(Energy_data)
Greenhouse_data, Greenhouse_data1 = read_file("C:/Users/HP/Documents/fname/greenhouse gas emission.py.xls") 
Greenhouse_data = filter_bar_data(Greenhouse_data)


Population_data,Population_data1=read_file("C:/Users/HP/Documents/fname/Population growth.xls")   
Population_data= filter_line_plot(Population_data)
Urban_pop_data, Urban_pop_data1 = read_file("C:/Users/HP/Documents/fname/urban population.xls")             
Urban_pop_data= filter_line_plot(Urban_pop_data)          



barplot(Energy_data, "Energy Use data (kg of oil equivalent per capita)","Total Forest Area")
barplot(Greenhouse_data, "Total greenhouse gas emission(kg of oil equivalent per capita)","Total greenhouse gas emission") 

line_plot(Population_data,"Population growth","Population growth (annual %)")
line_plot(Urban_pop_data,"Urban population (% of total population)","Urban population")