import warnings
warnings.filterwarnings("ignore")

import os
import time
import pandas as pd
import numpy as np

from utils import readChunk, toCSV

def main(data_dir, out_dir):
	for f in sorted(os.listdir(data_dir)):
		if f.endswith(".csv"):
			df = readChunk(os.path.join(data_dir, f))
			df = df[['USERID', 'SESSIONID', 'PRIMARY_FINGERPRINT', 'CONTENT_TYPE', 'SESSION_STARTDT_MONTH', 'SESSION_STARTDT_DAY', 'SESSION_STARTDT']]
			s = time.time()
			df['SESSION_STARTDT'] = pd.to_datetime(df['SESSION_STARTDT'])
			df['HOUR'] = df.SESSION_STARTDT.dt.hour
			e = time.time()
			total_time = time.strftime("%H:%M:%S", time.gmtime(e-s))
			print("Finish getting hour in {}".format(total_time))
			toCSV(df, os.path.join(out_dir, f), index = False)

if __name__ == '__main__':
	# main("../events/2018/12", "../events/december")
	main("../events/2019/01", "../events/january")
	main("../events/2019/02", "../events/february")
	main("../events/2019/03", "../events/march")
	main("../events/2019/04", "../events/april")
	main("../events/2019/05", "../events/may")