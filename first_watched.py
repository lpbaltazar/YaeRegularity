import warnings
warnings.filterwarnings("ignore")

import os
import time
import pandas as pd
import numpy as np

from utils import readChunk, toCSV

file = "all_month.csv"
usecols = ['USERID', 'CONTENT_TYPE', 'SESSION_STARTDT_MONTH', 'SESSION_STARTDT_DAY', 'STARTHOUR']
df = readChunk(file, usecols = usecols)

df = df.loc[df.SESSION_STARTDT_MONTH != '11']
convert = {'12':'0'}
df.replace({'SESSION_STARTDT_MONTH':convert}, inplace = True)
toint = ['SESSION_STARTDT_MONTH', 'SESSION_STARTDT_DAY', 'STARTHOUR']
for i in toint:
	df[i] = df[i].astype(int)
df['ORDER'] = (df.SESSION_STARTDT_MONTH*100)+(df.SESSION_STARTDT_DAY*10)

df.sort_values('ORDER', inplace = True)

print(len(df))
df.drop_duplicates(subset = ['USERID'], keep = 'first', inplace = True)
print(len(df))
print(df.head(20))
labels = pd.read_csv('clustering_6.csv')
labels.columns = labels.columns.str.upper()

df = df.merge(labels, how = 'left', on = 'USERID')

for i in df.LABEL.unique():
	print(i)
	temp = df.loc[df.LABEL == i]
	new_df = pd.DataFrame(index = list(range(1, 11)), columns = list(range(0, 6)))
	for j in df.CONTENT_TYPE.unique():
		for k in df.SESSION_STARTDT_MONTH.unique():
			temp2 = temp.loc[(temp.CONTENT_TYPE == j) & (temp.SESSION_STARTDT_MONTH == k)]
			new_df.loc[int(j)][k] = len(temp2)

	print(new_df)
	new_df.index.name = 'CONTENT_TYPE'
	toCSV(new_df, 'results/firstwatched/'+str(i)+'.csv')