import pandas as pd
import numpy as np
import csv
import datetime
import pandas_add

csv_file = 'expenses.csv'
source_csv = 'Untitled 1.csv'
df_exp = pd.read_csv(csv_file, sep=',')
source = pd.read_csv(source_csv, sep=',')
added = []
year = ' 2019'
lastId = df_exp.ID.max()
x = 0
y = 1

def deleteAll(csv_file):
    appender = ['item,price,date purchase (D MM),tid']
    target = open(csv_file, 'w')
    x = 0

    while x != len(appender):
        target.write(appender[x])
        x += 1

if len(source.index) > 0:
    while x != (len(source.index)):

        Next_ID = lastId + y
        ItemName = source.iloc[x, 0]
        Price = source.iloc[x, 1]
        DoP = source.iloc[x, 2] + year
        TID = source.iloc[x, 3]
        added.append(str(Next_ID) + ',' + ItemName + ',' + str(Price) + ',' + str(DoP) + ',' + str(TID) + ',' + str(datetime.datetime.today().strftime("%#d %m %Y")))
        y += 1
        x += 1

    pandas_add.writ(added, csv_file)
    deleteAll(source_csv)

print(str(len(source.index)) + ' has been added in expenses.csv')
