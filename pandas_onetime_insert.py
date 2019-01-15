import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy.sql import text
from datetime import datetime

metadata = MetaData()
engine = create_engine('sqlite:///C:\\Users\\Jemak\\Desktop\\Pandas\\pandas.db', echo=True)
conn = engine.connect()

#DEFINE the dataframes
df_exp = pd.read_csv('C://Users//Jemak//Desktop//pandas//expenses.csv', sep=',')
df_type = pd.read_csv('C://Users//Jemak//Desktop//pandas//type.csv', sep=',')

df_exp_208 = pd.read_csv('C://Users//Jemak//Desktop//pandas//expenses_2018.csv', sep=',')

df_inc = pd.read_csv('C://Users//Jemak//Desktop//pandas//income.csv', sep=',')
df_inctype = pd.read_csv('C://Users//Jemak//Desktop//pandas//TypeInc.csv', sep=',')


#EDIT dataframes date
df_inc.DateofPurchase = pd.to_datetime(df_inc.DateofPurchase, dayfirst=True)
df_inc.DateRecorded = pd.to_datetime(df_inc.DateRecorded, dayfirst=True)

df_exp_208.DateofPurchase = pd.to_datetime(df_exp_208.DateofPurchase, dayfirst=True)
df_exp_208.DateRecorded = pd.to_datetime(df_exp_208.DateRecorded, dayfirst=True)

df_exp.DateofPurchase = pd.to_datetime(df_exp.DateofPurchase, dayfirst=True)
df_exp.DateRecorded = pd.to_datetime(df_exp.DateRecorded, dayfirst=True)

#EXPENSES TYPE
ins1 = text('insert into expensesType (ID, TypeName, Description) values(:id, :name, :desc)')

for x in range(len(df_type)):
    conn.execute(ins1, id=int(df_type.iloc[x,0]), name=df_type.iloc[x,1], desc=df_type.iloc[x,2])

#EXPENSES 2008
ins208 = text('insert into expenses values (:id, :itemname, :price, :dop, :tid, :daterecorded)')

for x in range(len(df_exp_208)):
    conn.execute(ins208, id=int(df_exp_208.iloc[x,0]), itemname=df_exp_208.iloc[x,1],price=int(df_exp_208.iloc[x,2]),dop=str(df_exp_208.iloc[x,3]),tid=int(df_exp_208.iloc[x,4]),daterecorded=str(df_exp_208.iloc[x,5]))


x = 0

#EXPENSES
ins = text('insert into expenses values (:id, :itemname, :price, :dop, :tid, :daterecorded)')

for x in range(len(df_exp)):
    conn.execute(ins, id=int(df_exp.iloc[x,0]), itemname=df_exp.iloc[x,1],price=int(df_exp.iloc[x,2]),dop=str(df_exp.iloc[x,3]),tid=int(df_exp.iloc[x,4]),daterecorded=str(df_exp.iloc[x,5]))



#INCOMETYPE
x=0
ins2 = text('insert into incomeType (ID, TypeName, Description) values(:id, :name, :desc)')

for x in range(len(df_inctype)):
    conn.execute(ins2, id=int(df_inctype.iloc[x,0]), name=df_inctype.iloc[x,1], desc=df_inctype.iloc[x,2])


#INCOME
x = 0
ins3 = text('insert into income values (:id, :itemname, :price, :dop, :tid, :daterecorded)')

for x in range(len(df_inc)):
    conn.execute(ins3, id=int(df_inc.iloc[x,0]), itemname=df_inc.iloc[x,1],price=int(df_inc.iloc[x,2]),dop=str(df_inc.iloc[x,3]),tid=int(df_inc.iloc[x,4]),daterecorded=str(df_inc.iloc[x,5]))