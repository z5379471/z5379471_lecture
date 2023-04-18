import os
import pandas as pd

directory = '/Users/zhouyaqi/PycharmProjects/toolkit/config.TICMAP'
for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        CSVLOC = os.path.join(directory, filename)
        prc = pd.read_csv(CSVLOC)
        prc = pd.read_csv(CSVLOC, parse_dates=['Date'], index_col='Date')
        prc.sort_index(inplace=True)
        rets = prc.loc['2020'].loc[:, 'Close'].pct_change()
        avg_rets = rets.mean()
        print(avg_rets)

# --> 0.010015383194264737 the highest one: 'tsla'

