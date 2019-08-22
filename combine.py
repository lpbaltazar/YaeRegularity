import warnings
warnings.filterwarnings("ignore")

import os
import time
import pandas as pd
import numpy as np

from utils import readChunk, toCSV

def combineMonth(data_dir):
	all_df = []
	for f in sorted(os.listdir(data_dir)):
		if f.endswith(".csv"):
			df = readChunk(os.path.join(data_dir, f))
			all_df.append(df)
	all_df = pd.concat(all_df)
	print(len(all_df))

if __name__ == '__main__':
	combineMonth("../events/december")
	# main("../events/2019/01", "../events/january")
	# main("../events/2019/02", "../events/february")
	# main("../events/2019/03", "../events/march")
	# main("../events/2019/04", "../events/april")
	# main("../events/2019/05", "../events/may")