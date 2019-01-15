import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy.sql import text
import numpy as np
import csv
import datetime

metadata = MetaData()
engine = create_engine('sqlite:///C:\\Users\\Jemak\\Desktop\\Pandas\\pandas.db', echo=True)
conn = engine.connect()

source_csv = 'C://Users//Jemak//Desktop//Google_Drive//Untitled 1.csv'
source = pd.read_csv(source_csv, sep=',')
df_exp = pd.read_sql('select * from expenses', con=conn)

source_csv1 = 'C://Users//Jemak//Desktop//Google_Drive//Untitled 1 - Copy.csv'
source1 = pd.read_csv(source_csv1, sep=',')
df_inc = pd.read_sql('select * from income', con=conn)

added = []

x = 0
y = 1

def deleteAll(csv_file):
    appender = ['item,price,date purchase (YYYY-MM-DD),tid']
    target = open(csv_file, 'w')
    z = 0
    while z != len(appender):
        target.write(appender[z])
        z += 1

def writeAdded(added, lista):
    ins = text('insert into ' + lista + ' values (:id, :itemname, :price, :dop, :tid, :daterecorded)')
    for x in range(len(added)):
        conn.execute(ins, id=added[x][0], itemname=added[x][1], price=added[x][2], dop=added[x][3], tid=added[x][4], daterecorded=added[x][5])

def main():
    whole(source, df_exp, source_csv, 'expenses')
    whole(source1, df_inc, source_csv1, 'income')

def whole(sour, db_df, csv, tab):
    global x, y, added
    if len(sour.index) > 0:
        while x != (len(sour.index)):
            Next_ID = db_df.ID.max() + y
            ItemName = sour.iloc[x, 0]
            Price = sour.iloc[x, 1]
            DoP = pd.to_datetime(sour.iloc[x, 2], dayfirst=True)
            TID = sour.iloc[x, 3]
            added.append([int(Next_ID) , ItemName , int(Price) , str(DoP) , int(TID) , str(
                datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S"))])
            y += 1
            x += 1

        writeAdded(added, tab)
        deleteAll(csv)

    print(str(len(sour.index)) + ' item(s) has been added in ' + tab)
    added = []
    x = 0
    y = 1

if __name__ == '__main__':
    main()