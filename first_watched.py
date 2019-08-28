import warnings
warnings.filterwarnings("ignore")

import os
import time
import pandas as pd
import numpy as np

from utils import readChunk

file = "all_month.csv"
df = readChunk(file)

to_int = ['SESSION_STARTDT_MONTH', 'SESSION_STARTDT_DAY', 'STARTHOUR']


df = df.loc[df.SESSION_STARTDT_MONTH != '11']
df['SESSION_STARTDT_MONTH'] = df['SESSION_STARTDT_MONTH'].apply(lambda x: '0' if x == '12' else x)

df['ORDER'] = df.SESSION_STARTDT_MONTH+df.SESSION_STARTDT_DAY+df.STARTHOUR
df.ORDER = df.ORDER.astype(int)

df.sort_values('ORDER', inplace = True)

print(len(df))
df.drop_duplicates(subset = ['USERID'], keep = 'first', inplace = True)
print(len(df))