Original file is located at
    https://colab.research.google.com/drive/1bI-qoya-7bGCoenj3fiW60Ft9hPieX6_

Q1a
"""

import pandas as pd
path = "/content/drive/MyDrive/dslab02data/data1.csv"
df1=pd.read_csv(path, index_col=0)
path2 = "/content/drive/MyDrive/dslab02data/data2.csv"
df2 = pd.read_csv(path2, index_col=1)
print("Df1:\n", df1)
print("Df2:\n", df2)

"""Q1b"""

df3=pd.concat([df1,df2])
print(df3)

"""Q1c"""

path3="/content/drive/MyDrive/dslab02data/data3.csv"
df4=pd.read_csv(path3, usecols=["D", "E"])
print(df4)
df5=pd.concat([df3, df4], axis=1)
print('\nMerged: \n', df5)

"""Q1d & e"""

path4 = "/content/drive/MyDrive/dslab02data/data.json"
df6=pd.read_json(path4)
df7=pd.concat([df6,df5])
df7=df7.apply(pd.to_numeric, errors='coerce')
print(df7)

"""Q1e"""

df7 = df7.fillna(df7.mean())
df7.to_csv("newdata.csv")
df7 = df7.round(2)
print(df7)
