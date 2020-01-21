import numpy as np
import pandas as pd
df=pd.read_csv('new.csv',usecols=['name','score'])
print(df)
df.to_csv('edit.csv', encoding='utf-8', index=False ,sep='\t')
