# EDA の共通関数

import pandas as pd
import numpy as np


def stats(df):

	maxx = []
	minn = []

	for col in df.columns:
		maxx.append(df[col].value_counts().max())
		minn.append(df[col].value_counts().min())

	return pd.DataFrame(
		{'nunique': df.nunique(),
		 'len': len(df), 
		 'types': df.dtypes, 
		 'nulls': df.isna().sum(), 
		 'value counts max': maxx, 
		 'value counts min': minn},
		 columns = ['nunique', 'len', 'types', 'nulls', 'value counts max', 'value counts min']
		 )