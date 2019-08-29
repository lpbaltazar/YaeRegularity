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


content_type = {'ABS-CBN - Show - Current': 1, 'ABS-CBN - Show - Old':2, 'Original Show':3, 'Original Movie':4, 'Movie':5, 'Live':6, 'Fast Cut':7, 'Other - Show':8, 'Preview':9, 'Trailer':10}
keepcols = ['USERID', 'SESSIONID', 'CONTENT_TYPE', 'VIDEO_CATEGORY_TITLE', 'SESSION_STARTDT_MONTH', 'SESSION_STARTDT_DAY', 'STARTHOUR', 'ENDHOUR', 'DAY']


def getCustomerDay(month, date):
	if month == 12:
		return date
	elif month == 1:
		return date+31
	elif month == 2:
		return date+31+31
	elif month == 3:
		return date+31+31+28
	elif month == 4:
		return date+31+31+28+31
	else:
		return date+31+31+28+31+30

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
				df.CONTENT_TYPE = df.CONTENT_TYPE.astype(str)
				df.SESSION_STARTDT_MONTH = df.SESSION_STARTDT_MONTH.astype(int)
				df.SESSION_STARTDT_DAY = df.SESSION_STARTDT_DAY.astype(int)
				df = df.loc[df.SESSION_STARTDT_MONTH != 11]
				df['DAY'] = df[['SESSION_STARTDT_MONTH', 'SESSION_STARTDT_DAY']].apply(lambda x: getCustomerDay(x[0], x[1]), axis = 1)
				df = df.loc[df.CONTENT_TYPE != 'nan']

				df.replace({'CONTENT_TYPE':content_type}, inplace = True)
			all_df.append(df)
	all_df = pd.concat(all_df)
	all_df = all_df[keepcols]
	toCSV(all_df, outfile, index = False)

if __name__ == '__main__':
	combineMonth("../events/december", "results/december_customers.csv", check_login = True)
	combineMonth("../events/january", "results/january_customers.csv", check_login = True)
	combineMonth("../events/february", "results/february_customers.csv", check_login = True)
	combineMonth("../events/march", "results/march_customers.csv", check_login = True)
	combineMonth("../events/april", "results/april_customers.csv", check_login = True)
	combineMonth("../events/may", "results/may_customers.csv", check_login = True)

	combineMonth("results", "all_month.csv")
