#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 14:43:18 2018

@author: srikanth
"""
import numpy as np
import pandas as pd
lables=['a','b','c']
my_data=[10,20,30]
arr=np.array(my_data)
d={'a':10,'b':20,'c':30}

print(d)

print(pd.Series(data=my_data,index=lables ))
print(pd.Series(my_data,lables))
print(pd.Series(arr,lables))
