import pandas as pd
import mysql.connector

df = pd.read_csv("C:/Users/anubh/Downloads/Social_Network_Ads.csv")

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="xpdb"
)
cursor = conn.cursor()

cursor.execute("SELECT * FROM Social_Network_Ads") 
rows = cursor.fetchall()

df=pd.DataFrame(rows, columns=[i[0] for i in cursor.description])

cursor.close()
conn.close()

print(df.head())
