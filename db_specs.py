from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, BigInteger, String, Date, DateTime, MetaData, ForeignKey
import time
from sqlalchemy.sql import text

metadata = MetaData()
engine = create_engine('sqlite:///C:\\Users\\Jemak\\Desktop\\Pandas\\pandas.db', echo=True)

conn = engine.connect()

expenses = Table('expenses', metadata,
                 Column('ID', Integer, primary_key=True),
                 Column('ItemName', String),
                 Column('Price', BigInteger),
                 Column('DatePurchased', Date),
                 Column('TID', None, ForeignKey('expensesType.ID')),
                 Column('DateRecorded', DateTime)
                 )

expensesType = Table('expensesType', metadata,
                     Column('ID', Integer, primary_key=True),
                     Column('TypeName',String),
                     Column('Description', String)
                     )


expenses.create(engine)
print('Expense table has been created')
time.sleep(1)
expensesType.create(engine)
print('Expense Type table has been created')
time.sleep(1)