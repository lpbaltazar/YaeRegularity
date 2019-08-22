import warnings
warnings.filterwarnings("ignore")

import os
import time
import pandas as pd
import numpy as np

from utils import readChunk
from matplotlib import pyplot as plt
import seaborn as sns

import matplotlib.style as style

sns.set()
style.use('seaborn-poster')
style.use('bmh')

file = "../content_regularity.csv"

df = readChunk(file, header = None)
df.rename(columns = {0:'USERID', 1:'SESSION_ID', 2:'CONTENT_TYPE', 3:'PRIMARY_FINGERPRINT', 4:'SESSION_STARTDT_YEAR', 5:'SESSION_STARTDT_MONHT', 6:'SESSION_STARTDT_DAY', 7:'HOUR'}, inplace = True)
content_type = {'ABS-CBN - Show - Current': 1, 'ABS-CBN - Show - Old':2, 'Original Show':3, 'Original Movie':4, 'Movie':5, 'Live':6, 'Fast Cut':7, 'Other - Show':8, 'Preview':9, 'Trailer':10}

df.CONTENT_TYPE = df.CONTENT_TYPE.astype(str)
df.SESSION_STARTDT_MONTH = df.SESSION_STARTDT_MONTH.astype(int)
df.SESSION_STARTDT_DAY = df.SESSION_STARTDT_DAY.astype(int)
df.HOUR = df.HOUR.astype(int)
df = df.loc[df.CONTENT_TYPE != 'nan']

df.replace({'CONTENT_TYPE':content_type}, inplace = True)
print(df.head())

def getCustomerDay(month, date):
	if month == 12:
		return date
	elif month == 1:
		return date+31
	elif month == 2:
		return date+31+31
	elif month == 3:
		return date+31+31+28
	elif month == 4:
		return date+31+31+28+31
	else:
		return date+31+31+28+31+30
df['DAY'] = df[['SESSION_STARTDT_MONTH', 'SESSION_STARTDT_DAY']].apply(lambda x: getCustomerDay(x[0], x[1]), axis = 1)

count = 0
for user in df.USERID.unique():
	if count == 3: break
	temp = df.loc[df.USERID == user]
	new_df = pd.DataFrame(index = list(range(0, 24)), columns = list(range(1, 183)))
	for i in temp.index.unique():
		new_df.iloc[temp.loc[i]['HOUR']][temp.loc[i]['DAY']] = temp.loc[i]['CONTENT_TYPE']
	new_df.fillna(0, inplace = True)
	print(new_df.head(24))
	plot = sns.heatmap(new_df, fmt="d")
	plt.show()
	count = count+1
