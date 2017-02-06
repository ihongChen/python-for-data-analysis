# encoding:utf8

import pandas as pd
## group by ##
df = pd.DataFrame(
    {
        'key1':['a','a','b','b','a'],
        'key2':['one','two','one','two','one'],
        'data1':np.random.randn(5),
        'data2':np.random.randn(5)
    })
df

grouped = df['data1'].groupby(df['key1'])
grouped
grouped.mean()
means = df['data1'].groupby([df['key1'],df['key2']]).mean()
means
means.unstack()

states = np.array(['Ohio','California','California','Ohio','Ohio'])
years = np.array([2005,2005,2006,2005,2006])
df['data1'].groupby([states,years]).mean()

df.groupby('key1').mean()
df.groupby(['key1','key2']).mean()
df.groupby(['key1','key2']).size()

## Iterating over groups ##
for name,group in df.groupby('key1'):
    print(name)
    print(group)
