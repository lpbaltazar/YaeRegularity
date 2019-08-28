import warnings
warnings.filterwarnings("ignore")

import os
import time
import pandas as pd
import numpy as np

from utils import readChunk, toCSV
# import matplotlib as mpl
# mpl.use('tKagg')
from matplotlib import pyplot as plt
import seaborn as sns

import matplotlib.style as style

sns.set()
style.use('seaborn-poster')
style.use('bmh')

file = '../data/072A34C9427A4C15B0ED31FE6BEC48D8.csv'
data_dir = 'visualization/champs'

for f in sorted(os.listdir(data_dir)):
	if f.endswith(".csv"):
		df = pd.read_csv(file)
		plt.figure(figsize = (20, 9))
		df.replace(hour, inplace = True)
		df.set_index('HOUR', inplace = True)
		df.replace(0, np.nan, inplace = True)
		plot = sns.heatmap(df, annot = True, cbar = False, annot_kws={"fontsize":7}, vmin = 0, vmax = 10)
		plot.set_xlabel('DAYS')
		plot.set_yticklabels(['12MN','1AM','2AM','3AM','4AM','5AM','6AM','7AM','8AM','9AM','10AM','11AM','12NN','1PM','2PM','3PM','4PM','5PM','6PM','7PM','8PM','9PM','10PM','11PM'])
		plot.set_ylabel('TIME')
		plt.yticks(fontsize=10, rotation=360)
		plt.xticks(fontsize=8)
		plt.vlines([31, 62, 90, 121, 151], *plot.get_ylim())
		plt.savefig(data_dir+"/figures"+f[:-4]+".png")

# unique = []
# for i in df.columns:
# 	unique.extend(df[i].unique())

# for i in list(set(unique)):
# 	value = 0
# 	for j in df.columns:
# 		temp = df.loc[df[j] == i]
# 		value = value + len(temp)
# 	print(i, value)