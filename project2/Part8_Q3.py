import os
import pandas as pd
PRJDIR = '/Users/zhouyaqi/PycharmProjects/toolkit'
DATADIR = os.path.join(PRJDIR, 'config.TICMAP')
# as Q1, the highest average daily return in 2020 is tsla stock.
CSVLOC = os.path.join(DATADIR, 'tsla_prc.csv')
prc = pd.read_csv(CSVLOC)
prc = pd.read_csv(CSVLOC, parse_dates=['Date'], index_col='Date')
prc.sort_index(inplace=True)
rets = prc.loc['2010-01-01':'2020-12-31'].loc[:, 'Close'].pct_change()
annualised_returns_tsla = rets.mean() * 252
print(annualised_returns_tsla)

#--> 0.596892332164637