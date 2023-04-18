#import the modules
import os
import pandas as pd
#read the path
file_path = "/Users/zhouyaqi/PycharmProjects/toolkit/config.TICMAP"
#list all the files from the directory
file_list = os.listdir(file_path)
print(file_list)

df_append = pd.DataFrame()
#append all files together
for file in file_list:
            df_temp = pd.read_csv(file)
            df_append = df_append.append(df_temp, ignore_index=True)
