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

data_dir =  'results/firstwatched/'

for f in sorted(os.listdir(data_dir)):
	if f.endswith(".csv"):
		df = pd.read_csv(os.path.join(data_dir, f))
		# df.CONTENT_TYPE = df.CONTENT_TYPE.astype(str)
		plot = sns.barplot(x = 'COUNT', y = 'CONTENT_TYPE', data = df, orient = 'h', palette = 'Set3')
		# plot = df.plot(kind = 'bar', colormap = 'Set3')
		tot = df.COUNT.sum()
		df['percent'] = (df['COUNT']/tot)*100
		df['percent'] = df['percent'].astype(float)
		df['percent'] = round(df['percent'], 1)
		for p in plot.patches:
			width = p.get_width()
			plt.text(p.get_width(), p.get_y()+0.55*p.get_height(), '{:1.0f}'.format(width), va = 'center')
		# for i in range(df.shape[0]):
		# 	plot.text(i, df.iloc[i]['COUNT'], str(df.iloc[i]['percent']), horizontalalignment = 'center')
		plot.set_yticklabels(['ABS-CBN - Show - Current', 'ABS-CBN - Show - Old', 'Original Show', 'Original Movie', 'Movie', 'Live', 'Fast Cut', 'Other - Show', 'Preview', 'Trailer'])
		plot.set_ylabel('')
		plt.tight_layout()
		plt.savefig(data_dir+f[:-4]+'.png', dpi = 600)