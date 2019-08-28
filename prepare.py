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

def extractUser(users, df, outdir):
	for user in df.USERID.unique():
		if user in users:
			print(user)
			temp = df.loc[df.USERID == user]
			new_df = pd.DataFrame(index = list(range(0, 24)), columns = list(range(1, 183)))
			for i in temp.index.unique():
				for j in range(temp.loc[i]['STARTHOUR'], temp.loc[i]['ENDHOUR']+1):
					new_df.iloc[temp.loc[i][j]][temp.loc[i]['DAY']] = temp.loc[i]['CONTENT_TYPE']
			new_df.index.name = 'HOUR'
			new_df.fillna(0, inplace = True)
			toCSV(new_df, outdir+user+".csv")

if __name__ == '__main__':
	file = "all_month.csv"
	df = readChunk(file)
	# df.rename(columns = {0:'USERID', 1:'SESSION_ID', 2:'CONTENT_TYPE', 3:'PRIMARY_FINGERPRINT', 4:'SESSION_STARTDT_YEAR', 5:'SESSION_STARTDT_MONTH', 6:'SESSION_STARTDT_DAY', 7:'HOUR'}, inplace = True)

	df.CONTENT_TYPE = df.CONTENT_TYPE.astype(int)
	df.DAY = df.DAY.astype(int)
	df.HOUR = df.HOUR.astype(int)

	extractUser(["0013292CF87E70A73CF297C5D153C223", "008C58D802A70B19D6213C4860508135", "025A6C92BF0E4510972E82D220FBEACA", 
					"05EF69C6197E4C17990A12655C4C07DC", "6DE572EE144640C1BB76CFC3CFAA3036"],
					df, "visualization/champions/")

	extractUser(["0000E7E2BB754EFFB705B27E694C480B", "0010DA617A4F3B4F6E5E3A7D551B052A", "011E43952E214431944C5D423DBDF1BC", 
					"0004B4921F9E440089F42571DA8E3E9B", "0381FE4E93F240DFA4399E05D3DED7B4", "0AEA86E4E0784B9698688286005EA787"],
					df, "visualization/loyal/")

	extractUser(["00031E3E72758567C07D7A1E20034D16", "00054568469F4865985C2D296E4F6077", "003B4A26B2A7553D34A875C0B5B6808A",
					"00101B39BCB542A68D9AA6EB8130235A", "00244F3F5D75462FB71BFF19E2A41B27", "01AB096E84DEA722BFBE830E4C43D268"],
					df, "visualization/promising/")

	extractUser(["0000C7F70D7C462195FCFE8FBFAB4425", "00002017DDAEC61E44C09DA4DAE4F6B2", "0002069B1B884411A24BC3E7C9FA5163", 
					"000074E098804694A614C74837ED6E29", "0003DF3CC1A2402A898802B98E25F6D5", "0006EA84C607525EED985C60E7E95DE9"],
					df, "visualization/atrisk/")

	extractUser(["00004BAF4E2649D6BBB38749EFD1AD2F", "000248756C6A6B19C971E2BD3825D2D1", "000467039E34EC85B653F909D748F84B", 
					"0000B1700E224623AEA48ECEB0138BCE", "0000A066077762A1AC24919ABF275441", "00075BF0326E4087BC442DA25988FE1A"],
					df, "visualization/binge/")

	extractUser(["00001211E5EC40419CB8ACA6DF0ECFF5", "0000752E5B5244E8805F04AA5D6586AB", "000079E9CD574E6AA77160F2E0BF3276", 
					"00000FB8-F90A-43DA-8DEB-676678AE278C", "00002E9D-66F3-4B46-9702-E94E295BB291", "0000151C5F854009A6042ACBED1A0BC7"],
					df, "visualization/lost/")

