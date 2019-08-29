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

fig, axes = plt.subplots(nrows = 6)
count = 0
for f in sorted(os.listdir(data_dir)):
	if f.endswith(".csv"):
		df = pd.read_csv(os.path.join(data_dir, f))
		# df.CONTENT_TYPE = df.CONTENT_TYPE.astype(str)
		df.set_index('CONTENT_TYPE', inplace = True)
		df.T.plot(kind = 'barh', colormap = 'Set3', rot = 0, ax = axes[count])
		# plot = df.plot(kind = 'bar', colormap = 'Set3')
		# for p in plot.patches:
		# 	width = p.get_width()
		# 	plt.text(p.get_width(), p.get_y()+0.55*p.get_height(), '{:1.0f}'.format(width), va = 'center')
		# for i in range(df.shape[0]):
		# 	plot.text(i, df.iloc[i]['COUNT'], str(df.iloc[i]['percent']), horizontalalignment = 'center')
		count = count + 1
plt.show()
		# plot.legend(['ABS-CBN - Show - Current', 'ABS-CBN - Show - Old', 'Original Show', 'Original Movie', 'Movie', 'Live', 'Fast Cut', 'Other - Show', 'Preview', 'Trailer'])
		# plot.set_yticklabels(['DECEMBER', 'JANUARY', 'FEBRUARY', 'MARCH', 'APRIL', 'MAY'])
		# # plot.set_ylabel('')
		# plt.tight_layout()
		# # plt.show()
		# plt.savefig(data_dir+f[:-4]+'.png', dpi = 600)
		# plt.clf()