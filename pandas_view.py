import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import pandas_view_plot
from datetime import datetime

cur_mo = datetime.now().month

def what(wh):
    global df_, df_type,x
    if wh == 2019:
        while True:
            print()
            print('1. Expense')
            print('2. Income')
            print('0. Quit')
            print()
            x = int(input('What do you want to show? '))
            if x == 1:
                df_ = pd.read_csv('expenses.csv', sep=',')
                df_type = pd.read_csv('type.csv', sep=',')
                break
            elif x == 2:
                df_ = pd.read_csv('income.csv', sep=',')
                df_type = pd.read_csv('TypeInc.csv', sep=',')
                break
            elif x == 0:
                exit()
            else:
                print()
                print('Select a number.')
                print()

    elif wh == 2018:
        while True:
            print()
            print('1. Expense')
            print('2. Income')
            print('0. Quit')
            print()
            x = int(input('What do you want to show? '))
            if x == 1:
                df_ = pd.read_csv('expenses_2018.csv', sep=',')
                df_type = pd.read_csv('type.csv', sep=',')
                break
            elif x == 2:
                df_ = pd.read_csv('income_2018_incomplete.csv', sep=',')
                df_type = pd.read_csv('TypeInc.csv', sep=',')
                break
            elif x == 0:
                exit()
            else:
                print()
                print('Select a number.')
                print()

while 1==1:
    try:
        print()
        print('1. 2019')
        print('2. 2018')
        print('0. Quit')
        print()
        y = int(input('What Year do you want to show? '))
        if y == 1:
            yeer = 2019
            what(yeer)
            break
        elif y == 2:
            yeer = 2018
            what(yeer)
            break
        elif y == 0:
            exit()
        else:
            print()
            print('Select a correct year.')
            print()
    except ValueError:
        print()
        print('The input is incorrect!')
        print()

df = pd.merge(df_, df_type, left_on='TID', right_on='ID')
df.DateofPurchase = pd.to_datetime(df.DateofPurchase, dayfirst=True)
df.insert(4, 'Month', df.DateofPurchase.dt.month)

#df.insert(5, 'TypeCategory', 1)
#df.loc[(df['TID']==2) | (df['TID']==3) |(df['TID']==6) |(df['TID']==7) |
   #(df['TID']==8) |(df['TID']==9) |(df['TID']==13) , 'TypeCategory'] = 0

df = df[['ItemName', 'TypeName', 'Price', 'DateofPurchase', 'Month']]
df.Price = pd.to_numeric(df.Price)

#print(df.sort_values(by='DateofPurchase', ascending=False))
#print(df.sort_values(by='DateofPurchase', ascending=False).head(100))

tepm = df.groupby('Month', as_index=False).agg({'Price': np.sum})
repm = df[df.TypeName.isin([
    "Foods","Leisure","Toll, Gas, Parking, Commute",
    "Utilities, Bill, Rent","Consumables and Sevices",
    "Family Expenses","Sam"])].groupby('Month', as_index=False).agg({'Price': np.sum})
nrepm = df[df.TypeName.isin([
    'Gadget/Gear','One Time Expenses','Travel','Clothes','Medical', "Car Monthly",
    'Freelancing/Business Expense'])].groupby('Month', as_index=False).agg({'Price': np.sum})
nepm = df[df.TypeName.isin([
    "One Time Expenses", "Medical"])].groupby('Month', as_index=False).agg({'Price': np.sum})
lepm = df[df.TypeName.isin([
    "Clothes","Gadget/Gear","Travel"])].groupby('Month', as_index=False).agg({'Price': np.sum})
bepm = df[df.TypeName.isin([
    "Freelancing/Business Expense"])].groupby('Month', as_index=False).agg({'Price': np.sum})
max_m = repm.Month.max()
arepm = repm[repm['Month'] != max_m]
arepm = arepm.Price.mean()
etepm = df[df['Month'] == max_m].groupby('TypeName', as_index=False).agg({'Price': np.sum})
etepm1 = df[df['Month'] == (max_m - 1)].groupby('TypeName', as_index=False).agg({'Price': np.sum})
aetepm = df[df['Month'] != max_m].groupby('TypeName', as_index=False).agg({'Price': np.sum})

if x ==1 :
    for z in range(len(aetepm)):
        if max_m == 1:
            pass
        else:
            aetepm.Price[z] = aetepm.Price[z] / (max_m - 1)


metepm = df.groupby(['TypeName', 'Month'], as_index=False).agg({'Price': np.sum})
metepm1 = metepm[metepm['TypeName'] == 'Foods']
metepm2 = metepm[metepm['TypeName'] == 'Gadget/Gear']
metepm3 = metepm[metepm['TypeName'] == 'Car Monthly']
metepm4 = metepm[metepm['TypeName'] == 'Family Expenses']
metepm6 = metepm[metepm['TypeName'] == 'One Time Expenses']
metepm7 = metepm[metepm['TypeName'] == 'Travel']
metepm8 = metepm[metepm['TypeName'] == 'Clothes']
metepm9 = metepm[metepm['TypeName'] == 'Medical']
metepm10 = metepm[metepm['TypeName'] == 'Leisure']
metepm11 = metepm[metepm['TypeName'] == 'Sam']
metepm13 = metepm[metepm['TypeName'] == 'Freelancing/Business Expense']
metepm14 = metepm[metepm['TypeName'] == 'Utilities, Bill, Rent']
metepm15 = metepm[metepm['TypeName'] == 'Toll, Gas, Parking, Commute']
metepm16 = metepm[metepm['TypeName'] == 'Consumables and Sevices']
metepm17 = metepm[metepm['TypeName'] == 'Self Improvement']


#INCOME

tipm = df.groupby('Month', as_index=False).agg({'Price': np.sum})
aipm = tipm['Price'].sum(axis=0) / cur_mo

etim = df[df['Month'] == cur_mo].groupby('TypeName', as_index=False).agg({'Price': np.sum})
etim1 = df[df['Month'] == (cur_mo - 1)].groupby('TypeName', as_index=False).agg({'Price': np.sum})

aetipm = df[df['Month'] != max_m].groupby('TypeName', as_index=False).agg({'Price': np.sum})

metipm = df.groupby(['TypeName', 'Month'], as_index=False).agg({'Price': np.sum})
metipm1 = metipm[metipm['TypeName'] == 'Salary']
metipm2 = metipm[metipm['TypeName'] == 'Real Estate']
metipm3 = metipm[metipm['TypeName'] == 'PL']
metipm4 = metipm[metipm['TypeName'] == 'E Commerce']
metipm5 = metipm[metipm['TypeName'] == 'REM']

if x == 1:
    print('This is the sum of RECURRING expenses per month: ')
    print(repm)
    print('This is the sum of NON-RECURRING expenses per month: ')
    print(nrepm)
    print('This is the sum of NECESSARY expenses per month: ')
    print(nepm)
    print('This is the sum of LUHO expenses per month: ')
    print(lepm)
    print('This is the sum of BUSINESS expenses per month: ')
    print(bepm)
    print('This is the sum of TOTAL expenses per month: ')
    print(str(tepm))
    print('This is the average of RECURRING expenses per month: ')
    print(arepm)
    print('This is the total of EACH TYPE expenses this month: ')
    print(etepm)
    print('This is the total of EACH TYPE expenses LAST month: ')
    print(etepm1)
    print('This is the average of EACH TYPE expenses per month: ')
    print(aetepm)
else:
    print()
    print('This is the sum of Income per month: ')
    print(tipm)
    print()
    print('This is the average income per month: ' + str(aipm))
    print()
    print('This is the total of EACH TYPE of income this month: ')
    print(etim)
    print()
    if cur_mo == 1:
        pass
    else:
        print('This is the total of EACH TYPE income LAST month: ')
        print(etim1)
        print()
    print('This is the average of EACH TYPE of income per month: ')
    print(aetipm)
    print()

#with pd.option_context('display.max_rows', None):
 #   print(df[(df['Month'] == 1 ) & (df['TypeCategory'] == 0) ].sort_values('DateofPurchase', ascending=False))

plotting = pandas_view_plot


#df_exp.sort_values('DateofPurchase', ascending=True)
#print(df_exp.tail(50))
print(df_.tail(100).to_string())
