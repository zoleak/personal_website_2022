# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 07:04:44 2022

@author: kzolea

Continued EDA of fortune 1000 dataset
"""
# import environment
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import squarify # makes tree map
import seaborn as sns
###############################################################################
# Read in cvs file
df = pd.read_csv("Fortune_1000.csv")
###############################################################################
# Find out percent of woman CEOs
wf= df['ceo_woman'].value_counts(normalize=True).to_frame()
# Make pie chart of woman vs. men ceos
labels = "Male","Female"
plt.title("Percentage of Male Vs. Female CEOs")
plt.pie(wf["ceo_woman"],labels = labels, autopct = '%.1f%%',
        wedgeprops = {"edgecolor" : "black",
                      'linewidth': 1,
                      'antialiased': True})
###############################################################################
# Which states have the most fortune 1000 companies
state_count = df['state'].value_counts().rename_axis('state').reset_index(name = 'counts')
# Get top 10 states with the most companies
state_count = state_count.nlargest(20,'counts')
# Make tree map to show states with most fortune 1000 companies
sizes = state_count['counts']
labels =  [f'{state}\n{count}' for state, count in zip(state_count.state, state_count.counts)]
squarify.plot(sizes = sizes, label = labels, pad=True,
              color = 'mediumblue',text_kwargs={'color':'white'})
plt.axis('off')
plt.title('Top 10 States with the most headquarters')
plt.show() 
###############################################################################
#Which sectors have the most fortune 1000 companies
sector_count =  df['sector'].value_counts().rename_axis('sector').reset_index(name = 'counts')

###############################################################################
# Is there a relationship between # of employees and revenue?
sns.lmplot(x="revenue",y="num. of employees",
           data=df)
###############################################################################
# Profit vs. revenue in bar plot
rev_prof = df.nlargest(5,'revenue')
rev_prof = pd.melt(rev_prof,id_vars = ['company'],value_vars = ['revenue','profit'])
sns.set_theme(style="whitegrid")
sns.set_color_codes("pastel")
p1 =sns.barplot(x="value", y="company",hue = "variable",data= rev_prof)
p1.set_title("Profit Vs. Revenue for Top 5 Fortune 1000 Companies")
p1.set(xlabel='Millions ($)', ylabel="")

# Make table to put next to plot to show percent change in rev to prof
df2 = df.nlargest(5,'revenue')
#define custom function
def find_change(df2):
    change = (df2['profit']/df2['revenue'])*100
    return(change)
df3 = df2.groupby('company').apply(find_change).reset_index()
df3=df3.round()
#per_change = rev_prof.groupby('company','variable','value').assign(percent_change = (''))
# Put barplot and table together in same plot

plt.subplots_adjust(left=0.2, bottom=0.4)

the_table = plt.table(cellText=df3.values,
          cellLoc = 'center', rowLoc = 'center',
          transform=plt.gcf().transFigure,
          bbox = ([0.3, 0.1, 0.5, 0.2]))
the_table.auto_set_font_size(False)
the_table.set_fontsize(6)

###############################################################################
###############################################################################
###############################################################################


# Bar plot with top profitable companies with each logo at end




