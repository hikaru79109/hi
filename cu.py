# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 11:31:24 2017

@author: hikaru
"""

import pandas
from datetime import datetime
dfs=pandas.read_html('http://rate.bot.com.tw/xrt?Lang=zh-TW')
currency=dfs[0]
currency=currency.ix[:,0:5]
currency.columns=[u'幣別',u'現金匯率-本行買入',u'現金匯率-本行賣出', u'即期匯率-本行買入',u'即期匯率-本行賣出']
currency[u'幣別']=currency[u'幣別'].str.extract('\((\w+)\)')
currency['Date']= datetime.now().strftime('%Y-%m-%d')
currency['Date']=pandas.to_datetime(currency['Date'])

import sqlite3
with sqlite3.connect('D:\\currency.sqlite')as db:
    currency.to_sql('currency', con=db, if_exists='append')
