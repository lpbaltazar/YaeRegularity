import warnings
warnings.filterwarnings("ignore")

import os
import re
import time
import pandas as pd
import numpy as np

from utils import readChunk, toCSV


def removeNotLoggedIn(df):
	df["loggedin"] = df[["USERID", "PRIMARY_FINGERPRINT"]].apply(lambda x: 0 if re.search(x[1], x[0]) else 1, axis = 1)
	df = df.loc[df.loggedin == 1]
	print("logged in users: ", len(df))
	df.drop('loggedin', axis = 1, inplace = True)
	return df

def combineMonth(data_dir, outfile, check_login = False):
	all_df = []
	for f in sorted(os.listdir(data_dir)):
		if f.endswith(".csv"):
			df = readChunk(os.path.join(data_dir, f))
			df.dropna(subset = ['USERID'], inplace = True)
			if check_login:
				df.USERID = df.USERID.astype(str)
				df.PRIMARY_FINGERPRINT = df.PRIMARY_FINGERPRINT.astype(str)
				df = removeNotLoggedIn(df)
			all_df.append(df)
	all_df = pd.concat(all_df)
	toCSV(all_df, outfile, index = False)

if __name__ == '__main__':
	# combineMonth("../events/december", "results/december_customers.csv")
	# combineMonth("../events/january", "results/january_customers.csv")
	# combineMonth("../events/february", "results/february_customers.csv")
	# combineMonth("../events/march", "results/march_customers.csv")
	# combineMonth("../events/april", "results/april_customers.csv")
	# combineMonth("../events/may", "results/may_customers.csv")

	combineMonth("results", "all_month.csv")
