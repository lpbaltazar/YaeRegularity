import warnings
warnings.filterwarnings("ignore")

import os
import time
import pandas as pd
import numpy as np

from utils import readChunk, toCSV
# import matplotlib as mpl
# mpl.use('tKagg')
# mpl.rcParams['figure.dpi'] = 300
from matplotlib import pyplot as plt
import seaborn as sns

import matplotlib.style as style

sns.set()
style.use('seaborn-poster')
style.use('bmh')

def plotHeatmap(data_dir):
	for f in sorted(os.listdir(data_dir)):
		if f.endswith(".csv"):
			df = pd.read_csv(os.path.join(data_dir, f))
			# plt.figure(figsize = (20, 9))
			df.set_index('HOUR', inplace = True)
			df.replace(0, np.nan, inplace = True)
			plot = sns.heatmap(df, annot = True, cbar = False, annot_kws={"fontsize":5}, vmin = 1, vmax = 10, cmap = 'Set3')
			plot.set_xlabel('DAYS')
			plot.set_yticklabels(['12MN','1AM','2AM','3AM','4AM','5AM','6AM','7AM','8AM','9AM','10AM','11AM','12NN','1PM','2PM','3PM','4PM','5PM','6PM','7PM','8PM','9PM','10PM','11PM'])
			plot.set_ylabel('TIME')
			plt.yticks(fontsize=10, rotation=360)
			plt.xticks(fontsize=8)
			plt.vlines([31, 62, 90, 121, 151], *plot.get_ylim())
			plt.tight_layout()
			plt.savefig(data_dir+"/figures/"+f[:-4]+".png", dpi = 600)
			# plt.show()
			plt.clf()

# unique = []
# for i in df.columns:
# 	unique.extend(df[i].unique())

# for i in list(set(unique)):
# 	value = 0
# 	for j in df.columns:
# 		temp = df.loc[df[j] == i]
# 		value = value + len(temp)
# 	print(i, value)

if __name__ == '__main__':
	plotHeatmap("visualization/champions")
	plotHeatmap("visualization/loyal")
	plotHeatmap("visualization/promising")
	plotHeatmap("visualization/binge")
	plotHeatmap("visualization/atrisk")
	plotHeatmap("visualization/lost")