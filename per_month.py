import warnings
warnings.filterwarnings("ignore")

import os
import time
import pandas as pd
import numpy as np

from utils import readChunk, toCSV

content_type = 1
colname = 'frequency_'+str(content_type)
outfile = 'results/'+str(content_type)+'.csv'

data_dir = 'results'

def generateMonth():
	for f in sorted(os.listdir(data_dir)):
		if f.endswith(".csv"):
			file = os.path.join(data_dir, f)
			df = readChunk(file)
			df.CONTENT_TYPE = df.CONTENT_TYPE.astype(int)
			df.DAY = df.DAY.astype(int)
			df.SESSION_STARTDT_MONTH = df.SESSION_STARTDT_MONTH.astype(int)
			df = df.loc[df.SESSION_STARTDT_MONTH != 11]

			new_df = pd.DataFrame(index = df.USERID.unique())
			new_df.index.name = 'USERID'
			temp = df.loc[df.CONTENT_TYPE == content_type]
			for i in range(df.DAY.min(),df.DAY.max()+1):
				temp2 = temp.loc[temp.DAY == i]
				group = temp2.groupby(['USERID'])['DAY'].count().to_frame()
				group.DAY = group.DAY.apply(lambda x: np.nan if np.isnan(x) else '1')
				group.rename(columns = {'DAY':str(i)}, inplace = True)
				new_df = new_df.merge(group, how = 'left', on = 'USERID')
			toCSV(new_df, 'results/'+str(content_type)+f)

def func(x):
	if x.first_valid_index() is None:
		return np.nan
	else:
		return x.first_valid_index()

def combineMonth():
	new_df = pd.DataFrame
	for f in sorted(os.listdir(data_dir+'/'+str(content_type))):
		if f.endswith(".csv"):
			file = os.path.join(data_dir+'/'+str(content_type), f)
			if len(new_df) == 0:
				new_df = readChunk(file)
			else:
				df = readChunk(file)
				new_df = new_df.merge(df, how = 'left', on = 'USERID')

	new_df.set_index('USERID', inplace = True)
	new_df['first_occurence'] = new_df.apply(func, axis = 1)
	new_df.fillna('0', inplace = True)
	new_df['total'] = new_df['first_occurence'].apply(lambda x: '1'*(32-int(x)))
	new_df[cols] = new_df[cols].astype(str)
	new_df['all'] = new_df[cols].apply(''.join, axis = 1)
	print(new_df['total'])
	new_df[colname] = new_df[['all', 'total']].apply(lambda x: int(x[0], 2)/int(x[1], 2), axis = 1)
	print(new_df[colname])
	print(cols)
	cols.append(colname)
	print(cols)
	toCSV(new_df[cols], outfile, index = True)

if __name__ == '__main__':
	generateMonth()
	# combineMonth()
