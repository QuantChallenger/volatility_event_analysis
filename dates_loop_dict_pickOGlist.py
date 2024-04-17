# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 13:16:17 2024

@author: reyna
"""

#New idea pick up all the dates , find the most recurrent out of the 30 stocks, sort them datas, create a list. 
#Then create a dict out of each csv based on date as main key [close, volume]. Then only pick up the dates
# from your orignal list in a loop and store them in a list of df, then concat them and send to excel

import os
import pandas as pd

source = r'C:\Users\reyna\Desktop\VAR TEST MONTHLY' #VAR TEST DAILY or VAR TEST WEEKLY or VAR TEST MONTHLY

output_file = r'C:\Users\reyna\Desktop\fused documents\FusedmonthlyVar.xlsx' #FuseddailyVar or FusedweeklyVar or FusedmonthlyVar
test_file = r'C:\Users\reyna\Desktop\fused documents\test.xlsx'

"""
#Daily only

# Initialize an empty list to store DataFrames
dfs = []

# Iterate through each file in the directory
for filename in os.listdir(source):
    filepath = os.path.join(source, filename)
    if os.path.isfile(filepath) and filename.endswith('.csv'):
        # Read the CSV file
        data = pd.read_csv(filepath)
        # Select only the required columns
        selected_data = data[['Date']]
        # Append selected data to the list of DataFrames
        dfs.append(selected_data)

concatenated_data = pd.concat(dfs, axis= 0)


date_counts = concatenated_data['Date'].value_counts()





correct_dates = date_counts[date_counts >= 30] #no need for this part for weekly and monthly
correct_dates = correct_dates.sort_index(ascending = True)
correct_dates = correct_dates.to_dict()
key_data = list(correct_dates.keys())
list_key = pd.DataFrame(key_data)
list_key = list_key.rename(columns = { 0 :"date"})



#list_key.to_excel(test_file, index=True, header=True)
"""

df2 = []
# Iterate through each file in the directory
for filename in os.listdir(source):
    filepath = os.path.join(source, filename)
    if os.path.isfile(filepath) and filename.endswith('.csv'):
        # Read the CSV file
        data = pd.read_csv(filepath)
        # Select only the required columns
        selected_data = data[['Date','Close','Volume']]
        selected_data = selected_data.rename(columns={'Date': 'Date'})
        selected_data = selected_data.rename(columns={'Close': 'Close' + filename[:-4]})
        selected_data = selected_data.rename(columns={'Volume': 'Volume' + filename[:-4]})
        # Append selected data to the list of DataFrames
        df2.append(selected_data)

#This part is for monthly and weekly only
concate_data = pd.concat(df2, axis= 1)
correct_dates = concate_data.sort_index(ascending = True)

concate_data.to_excel(output_file, index=True, header=True)


'''
#This part of the codecode is for daily only


merged_dfs=[]

for df in df2:
    merged_df = list_key.merge(df, how= "inner", left_on ='date', right_on = 'Date')
    merged_dfs.append(merged_df)


final_merge = pd.concat(merged_dfs, axis= 1)
final_merge.to_excel(output_file, index=True, header=True)
print(final_merge)
'''




