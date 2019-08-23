import warnings
warnings.filterwarnings("ignore")

import os
import time
import pandas as pd
import numpy as np

from utils import readChunk, toCSV
import matplotlib as mpl
mpl.use('tKagg')
from matplotlib import pyplot as plt
import seaborn as sns

import matplotlib.style as style

sns.set()
style.use('seaborn-poster')
style.use('bmh')

file = "all_month.csv"

df = readChunk(file)
# df.rename(columns = {0:'USERID', 1:'SESSION_ID', 2:'CONTENT_TYPE', 3:'PRIMARY_FINGERPRINT', 4:'SESSION_STARTDT_YEAR', 5:'SESSION_STARTDT_MONTH', 6:'SESSION_STARTDT_DAY', 7:'HOUR'}, inplace = True)

df.CONTENT_TYPE = df.CONTENT_TYPE.astype(int)
df.DAY = df.DAY.astype(int)
df.HOUR = df.HOUR.astype(int)


for user in df.USERID.unique():
	temp = df.loc[df.USERID == user]
	new_df = pd.DataFrame(index = list(range(0, 24)), columns = list(range(1, 183)))
	for i in temp.index.unique():
		new_df.iloc[temp.loc[i]['HOUR']][temp.loc[i]['DAY']] = temp.loc[i]['CONTENT_TYPE']
	new_df.index.name = 'HOUR'
	new_df.fillna(0, inplace = True)
	toCSV(new_df, "visualization/"+user+".csv")
