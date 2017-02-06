# encoding:utf8
import pandas as pd
import MySQLdb

df = pd.read_csv('./pet.txt')
df
# 不能用這樣的conn 使用pd.to_sql(...,con)
# mysql_con= MySQLdb.connect(
#         host='ihongchen.ctbx4pq8or72.us-west-2.rds.amazonaws.com',
#         port=3306,user='ehome4829', passwd='a126234829',
#         db='menagerie',charset = 'utf8'
#         )

# df[['name','owner','species','sex']] = df[['name','owner','species','sex']].astype(str) #text
df[['name','owner','species','sex']] = df[['name','owner','species','sex']].astype(sqlalchemy.dialects.mysql.VARCHAR) #text
df['birth'] = df['birth'].astype('datetime64[ns]')
df['death'] = df['death'].astype('datetime64[ns]')
df2 = pd.DataFrame(
            [[u'小黑狗',u'陳一宏','dog','m','2011-01-03']],
            columns=['name','owner','species','sex','birth']
            )
df2
df = df.append(df2,ignore_index=True)
df


import sqlalchemy
from sqlalchemy.dialects.mysql import VARCHAR,NVARCHAR
from sqlalchemy import create_engine
dbname = 'menagerie'
connstr = "mysql+mysqldb://ehome4829:a126234829@ihongchen.ctbx4pq8or72.us-west-2.rds.amazonaws.com:3306/{}?charset=utf8".format(dbname) # 要加入?charset=utf8才不會亂碼
engine = create_engine(connstr)
conn = engine.connect()

df.to_sql('pet',conn,if_exists='replace',index=False,dtype={'name':NVARCHAR(20),'owner':NVARCHAR(20),'species':VARCHAR(5)})
df.to_sql('pet',conn,if_exists='replace',index=False) # 會變成text格式...
