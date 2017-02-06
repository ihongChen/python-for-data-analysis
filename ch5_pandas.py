# -*- coding: utf-8 -*-
"""
ex ch5.py
python for data analysis,

Created on Mon Jun 20 21:39:35 2016

@author: ihong
"""

import pandas as pd
import numpy as np

df = pd.DataFrame(
            np.random.randn(4,3),columns=list('bde'),index=['Utah','Ohio','Texas','Oragon'])

df = pd.DataFrame([[1.4,np.nan],[7.1,-4.5],[np.nan,np.nan],[0.75,-1.3]],
                  index=['a','b','c','d'],
                    columns = ['one','two'])

df
df.sum() ## colum sum,neglect nan!
df.sum(axis=1) ## row sum,neglect nan.
df.mean(axis=1,skipna=False) ##
df
df.idxmax() ## find index of max(col1,col2)
df
df.cumsum() ## accumaltion
df.describe() ## describe


obj = pd.Series(['a','b','c','a']*4)
obj.describe()
