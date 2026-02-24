import numpy as np
import pandas as pd

df=pd.read_csv('Social_Network_Ads.csv')
# print(df.head(2))

df=df.drop(columns=['User ID','Gender'])

x=df.drop(columns=['Purchased'])
y=df['Purchased']

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=2)

from sklearn.linear_model import LogisticRegression
lr=LogisticRegression()
lr.fit(x_train,y_train)

import joblib

joblib.dump(lr,'lr_model.pkl')
print('Model is saved as lr_model.pkl') 