import warnings
warnings.filterwarnings("ignore")

import os
import time
import pandas as pd
import numpy as np

from utils import readChunk, toCSV

def combineMonth(data_dir, outfile):
	all_df = []
	for f in sorted(os.listdir(data_dir)):
		if f.endswith(".csv"):
			df = readChunk(os.path.join(data_dir, f))
			all_df.append(df)
	all_df = pd.concat(all_df)
	toCSV(all_df, outfile, index = False)

if __name__ == '__main__':
	combineMonth("../events/december", "results/december_customers.csv")
	combineMonth("../events/january", "results/january_customers.csv")
	combineMonth("../events/february", "results/february_customers.csv")
	combineMonth("../events/march", "results/march_customers.csv")
	combineMonth("../events/april", "results/april_customers.csv")
	combineMonth("../events/may", "results/may_customers.csv")
