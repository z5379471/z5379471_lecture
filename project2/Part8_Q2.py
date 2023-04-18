
import os
import pandas as pd

directory = '/Users/zhouyaqi/PycharmProjects/toolkit/config.TICMAP'
for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        CSVLOC = os.path.join(directory, filename)
        prc = pd.read_csv(CSVLOC)
        prc = pd.read_csv(CSVLOC, parse_dates=['Date'], index_col='Date')
        prc.sort_index(inplace=True)
        rets = prc.loc['2010-01-01':'2020-12-31'].loc[:, 'Close'].pct_change()
        annualised_returns = rets.mean() * 252
        print(annualised_returns)

def Average(list):
    return sum(list) / len(list)
list = [0.09469987647760494,
0.10357914405812263,
0.22462943050780362,
0.596892332164637,
0.0913719982700778,
0.12835338313433975,
0.300050179906989,
0.1146249034139147,
0.15699655549798816,
0.21417319647635033,
0.22685860098720567,
0.24896082277912127,
0.1805721044332246,
0.08506466888523405,
0.38156600196255563,
0.2379329485826445,
0.4049953801728108,
0.0675164180748427,
0.156472258048532,
0.014757400782757375,
0.08215394483723153,
0.2947943026509459,
-0.016676314003322677]
EW = Average(list)
print(EW) #--> 0.19088432774354833