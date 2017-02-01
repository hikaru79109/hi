# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 12:53:33 2017

@author: hikaru
"""

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

fromaddr='hikaru79109@gmail.com'
toaddr='hikaru79109@hotmail.com'
PASSWD='twy79109'
msg =MIMEMultipart()
msg['From']=fromaddr
msg['To']=toaddr
msg['Subject']='[匯率觸價通知]'

import sqlite3, pandas
with sqlite3.connect('D:\\currency.sqlite') as db:
    df=pandas.read_sql_query(r'select * from currency where "幣別" = "JPY" order by Date'.decode('utf-8'),con=db)

#body='helloworld'
#msg.attach(MIMEText(body,'plain'))
msg.attach(MIMEText(df.to_html().encode('utf-8'),'html'))

server=smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, PASSWD)

text=msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()