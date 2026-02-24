import numpy as np
import pandas as pd

df=pd.read_csv('covid_toy - covid_toy.csv')
df=df.dropna()
#print(df.head(3))

from sklearn.preprocessing import LabelEncoder
lb= LabelEncoder()

df['cough']=lb.fit_transform(df['cough'])
df['city']=lb.fit_transform(df['city'])
df['has_covid']=lb.fit_transform(df['has_covid'])
df['gender']=lb.fit_transform(df['gender'])

#print(df.head(3))

x=df.drop(columns='has_covid')
y=df['has_covid']

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=2)

from sklearn.linear_model import LogisticRegression
lr=LogisticRegression()
lr.fit(x_train,y_train)

import joblib

joblib.dump(lr,'lr_model.pkl1')
print('Model is saved as lr_model.pkl1')