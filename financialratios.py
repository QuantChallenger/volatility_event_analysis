# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 19:27:57 2024

@author: reyna
"""

# 1) load produced dataframe, remove duplicated values and keep only 1
# 

import statsmodels.formula.api as smf
import pandas as pd

output_file = r'C:\Users\reyna\Desktop\fused documents\FuseddailyVar.xlsx' 
df = pd.read_excel(output_file, sheet_name="HistReturn")
#x= the stocks
#y= column__GRNUS

model=smf.ols('column_002594_SZ ~ column__GRNUS',df).fit()


b0=model.params[0]
b1=model.params[1]


#First way
prediction1=b0+b1*df['column__GRNUS']
prediction1.tail()

#Second way
prediction2 =model.predict(df)
prediction2.tail()

df['response']= model.predict(df)
df['error']=df['response'] - df['column_002594_SZ']
df.tail()

print(model.summary())

"""
#For Plots
import matplotlib.pyplot as plt

plt.scatter(df['column__GRNUS'],df['column_002594_SZ'])
plt.plot(df['column__GRNUS'],df['response'], color='r')
plt.show()

plt.scatter(df['column__GRNUS'],df['error'])
plt.scatter(df['column_002594_SZ'],df['response'])



"""