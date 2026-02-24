import mysql.connector
import pandas as pd

df=pd.read_csv("C:/Users/anubh/Downloads/Social_Network_Ads.csv")
conn = mysql.connector.connect(
    host="localhost",
    user="root",    
    password="1234",
    database="xpdb"
)
query='Select * from social_network_ads'
df=pd.read_sql(query, conn)

print(df.head())