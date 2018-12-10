#!/usr/bin/python

import os
import pandas as pd

# Open a file
path = "D:\PERSONAL\IMPORTANT\Resumes"
dirs = os.listdir( path )

# This would print all the files and directories
for file in dirs:
   print (file)

df = pd.DataFrame({'Data': [10, 20, 30, 20, 15, 30, 45]})

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Sheet1')

# Close the Pandas Excel writer and output the Excel file.
writer.save()

