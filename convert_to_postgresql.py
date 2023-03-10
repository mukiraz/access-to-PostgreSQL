# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 21:01:06 2023

@author: Murat Uğur KİRAZ
"""

import pandas as pd
import numpy as np
import os

#Parameters
access_to_postgre_csv_file = "100_salarychange.csv" # write down csv file
postgre_table_name = "public.personnel_salarychange"

# delete file if out output data exists
if os.path.exists("sql.txt"):
  os.remove("sql.txt")

# Import data from csv to pandas dataframe and if there is null data inside, fill them with "Null" string
data = pd.read_csv(access_to_postgre_csv_file, sep=";")
data = data.fillna("NULL")

#get the column and row number of the data
column_number = len(data.columns)
row_number = len(data)

# we will have column names and add column_str variable
column_names = list(data.columns.values)
column_str = ""
for column_name in column_names:
    column_str += column_name + ","
column_str = column_str[0:len(column_str)-1] # this will delete the last comma , ;)

# loop in columns and rows, append each row in appropriate PostgreSQL insert script format
# save in the sql.txt file
for i in range(row_number):
    row_str = ""
    for j in range(column_number):        
        #row_str += str(data.iloc[i,j]) + ","
        #print(type(data.iloc[i,j]), data.iloc[i,j])
        if type(data.iloc[i,j]) == np.str:
            if (data.iloc[i,j] == "NULL") or data.iloc[i,j] == "1900-01-00":
                row_str += "NULL, "
            else:
                row_str += "'" + str(data.iloc[i,j]) + "'" + ","
        else:
            row_str += str(data.iloc[i,j]) + ","
    row_str = row_str[0:len(row_str)-1]    
    sentence = "INSERT INTO {}({}) VALUES ({});\n".format(postgre_table_name, column_str, row_str)
    file = open("sql.txt" , "a", encoding=("UTF-8"))
    file.write(sentence)
    file.close()
    


