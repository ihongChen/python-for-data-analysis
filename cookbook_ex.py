#! encoding: utf8

import pandas as pd
import numpy as np
df = pd.DataFrame(
    {
        'AAA':[4,5,6,7],
        'BBB':[10,20,30,40],
        'CCC':[100,50,-30,-50]
    }
)
df
df.ix[df.AAA>=5]
df.ix[df.AAA>=5,'BBB'] = -1; df

df.dtypes

df['AAA'] = df['AAA'].astype(float)
df[['AAA','BBB']] = df[['AAA','BBB']].astype(float)
df.dtypes
## if-then...
df.ix[df.AAA>5,['BBB','CCC']] = 2000;df

df_mask = pd.DataFrame({'AAA':[True]*4,'BBB':[False]*4,'CCC':[True,False]*2})

df.where(df_mask,-1000)

np.where(df['AAA']>5)
df['logic'] = np.where(df['AAA']>5,'high','low')
df


# splitting #

df = pd.DataFrame({'AAA':[4,5,6,7],'BBB':[10,20,30,40],'CCC':[100,50,-30,-50]});df

dflow = df[df.AAA <=5]
dflow

dfhigh = df[df.AAA>5]
dfhigh


# Building Criteria

df = pd.DataFrame({'AAA':[4,5,6,7],'BBB':[10,20,30,40],'CCC':[100,50,-30,-50]});df
df['CCC']>=-40
df.loc[(df['BBB']<25) & (df['CCC']>= -40),'AAA']
df.ix[(df['BBB']<25) & (df['CCC']>= -40),'AAA']

df.ix[(df['BBB']<25) & (df['CCC']>= -40),'AAA'] = 0.1
df

## argsort
df = pd.DataFrame({'AAA':[4,5,6,7],'BBB':[10,20,30,40],'CCC':[100,50,-30,-50]});df
avalue = 43.0
df.ix[(df.CCC-avalue).abs().argsort()]
(df.CCC-avalue)
greater5 = lambda x:x>5
filter(greater5,[1,2,3,4,5,6,7,10])

## dynamic criteria
df = pd.DataFrame({'AAA':[4,5,6,7],'BBB':[10,20,30,40],'CCC':[100,50,-30,-50]});df
crit1 = df.AAA<=5.5
crit2 = df.BBB== 10.0
crit3 = df.CCC >-40
import functools
critList = [crit1,crit2,crit3]
AllCrit = functools.reduce(lambda x,y:x&y, critList)
reduce(lambda x,y:x+y,list(range(10)))
AllCrit = reduce(lambda x,y:x&y,critList)
df[AllCrit]


## Dataframe ##
df = pd.DataFrame({'AAA':[4,5,6,7],'BBB':[10,20,30,40],'CCC':[100,50,-30,-50]});df
df.index.isin([0,2,4])
df.AAA<=6
df.index = ['foo','bar','foo','kar']
df
df.ix[0:3]
df.ix['bar':'kar']
