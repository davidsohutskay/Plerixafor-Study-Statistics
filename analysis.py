# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 07:17:13 2022

@author: david
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import scipy as sp
import numpy as np

# gcsfOnly = pd.read_csv ('gcsfOnly.csv')
# mozOnFailure = pd.read_csv ('mozOnFailure.csv')
# mozUpfront = pd.read_csv ('mozUpfront.csv')

cleanedData = pd.read_csv ('cleanedData.csv')

cleanedData.head()

#######################################
## Plot the raw data
#######################################

ax = sns.violinplot(data=cleanedData, x="Group", y="Total collect", palette="Blues") # , inner = "points" , hue="alive"
sns.swarmplot(data=cleanedData, x ='Group', y ='Total collect', color = "black", alpha=0.7)
ax.set(xlabel='', ylabel='Total Collection ()')
plt.show()

#sns.violinplot(data=cleanedData, x="Group", y="CD34", palette="Blues") # , inner = "points" , hue="alive"
ax = sns.swarmplot(data=cleanedData, x ='Group', y ='CD34', color = "black")
ax.set(xlabel='', ylabel='CD34')
plt.show()

# sns.violinplot(data=cleanedData, x="Group", y="Total collect", palette="Blues") # , inner = "points" , hue="alive"
# sns.swarmplot(data=cleanedData, x ='Group', y ='Total collect', color = "black", alpha=0.7)
# plt.show()

#######################################
## Calculate some statistics
#######################################

stat, p = sp.stats.mannwhitneyu(cleanedData[cleanedData["Group"] == "GCSF"]["Total collect"].dropna(), cleanedData[cleanedData["Group"] == "MOZUPFRONT"]["Total collect"].dropna(), alternative='two-sided')

#stat, p = sp.stats.ttest_ind(cleanedData[cleanedData["Group"] == "GCSF"]["Total collect"].dropna(), cleanedData[cleanedData["Group"] == "MOZUPFRONT"]["Total collect"].dropna())

#######################################
## Plot the number of collection days
#######################################

cleanedData["Collection Number"] = [ord(x)-64 for x in cleanedData.Collection]

dayCounts = cleanedData.groupby(['Group', 'Collection Number']).size().reset_index(name='Counts')
firsts = (dayCounts.groupby('Group').transform('first'))["Counts"]
dayCounts["Normalized Counts"] = dayCounts["Counts"]/firsts

fig, ax = plt.subplots(figsize=(8,6))
dayCounts.groupby('Group').plot(x = "Collection Number", y = "Normalized Counts", ax=ax)
plt.show()

# countStats = cleanedData.groupby('Group')["Collection Number"].agg([np.mean, np.std])
# countStats["Group"] = countStats.index

ax = sns.barplot(data = cleanedData, x = "Group", y = "Collection Number", palette="Blues")
ax.set(xlabel='', ylabel='Number of Collection Days')
plt.show()