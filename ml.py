# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 15:47:28 2020

@author: Mohan

"""

import pandas as pd
df=pd.read_csv("music.csv")
print(type(df))
print(df.dtypes)
print(df.head(1))
print(df.tail(1))
print (df["age"].value_counts())
print(df.iloc[:,:-1])
print(df.loc[:,["age"]])
#print(df.iloc[:,:])
print([df["age"]>20])
df2=df.loc[df["age"]>20].head()
print(df2)
df3=df.loc[df["age"]==23]
print(df3)
df4=(df[df["age"].isin([23])].shape)
print(df.head(n=10))


