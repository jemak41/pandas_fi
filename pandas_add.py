import pandas as pd
import numpy as np
import csv
import datetime
df_exp = pd.read_csv('expenses.csv', sep=',')
df_type = pd.read_csv('type.csv', sep=',')
df_inc = pd.read_csv('income.csv', sep=',')
df_typeinc = pd.read_csv('TypeInc.csv', sep=',')
df = pd.merge(df_exp, df_type, left_on='TID', right_on='ID').sort_values('ID_x', ascending=True)
df_i = pd.merge(df_inc, df_typeinc, left_on='TID', right_on='ID')
df = df[['ID_x','ItemName', 'Price','DateofPurchase', 'TypeName']]
df_i = df_i[['ID_x','ItemName', 'Price','DateofPurchase', 'TypeName']]
added = []
type_list_exp = df_type[['ID', 'TypeName']]
type_list_inc = df_typeinc[['ID', 'TypeName']]
year = ' 2019'
def writ(added, csv_):
    target = open(csv_, 'a')
    for x in range(len(added)):
        target.write(added[x])
        if len(added) > 0:
            target.write('\n')
    target.close()
def append(dataf,csv_filename, csv_file, type_list, df_show):
    x = 1
    while True:
        print(df_show.tail(30))
        Next_ID = dataf.ID.max() + x
        ItemName = input('What did you buy/earn? ')
        #print(type_list.drop_duplicates())
        print(type_list)
        TID = input('Select the ID of Type: ')
        Price = input('How Much? ')
        DoP = input('When was the purchase? (D MM) ') + year
        added.append(str(Next_ID) + ',' + ItemName + ',' + Price + ',' + DoP + ',' + TID + ',' + datetime.datetime.today().strftime("%#d %m %Y") )
        again = input('Do you have another purchase/sales? ')
        x += 1
        if again == 'yes':
            pass
        else:
            writ(added, csv_file)
            break
    print('Purchase/Sales Added:')
    df = pd.read_csv(csv_filename, sep=',')
    print(df.tail(50))
    
def main():
    while True:
        try:
            print('1. Expenses')
            print('2. Income')
            print('0. Quit')
            adding = int(input('What do you want to add? '))
            if adding == 1:
                append(df_exp, 'expenses.csv', 'expenses.csv', type_list_exp, df)
            elif adding == 2:
                append(df_inc, 'income.csv', 'income.csv', type_list_inc, df_i)
            elif adding == 0:
                exit()
            else:
                print('Enter correct number.')
                continue
            print('1. Yes')
            print('2. No')
            validation = int(input('Do you want to add anything? '))
            if validation == 2:
                break
        except ValueError:
            print()
            print('The input is incorrect!')
            print()
            
if __name__ == '__main__':
    main()
