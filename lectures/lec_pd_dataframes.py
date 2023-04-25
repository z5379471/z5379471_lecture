""" lec_pd_dataframes.py

Companion codes for the lecture on Dataframes
"""

import pandas as pd
# --------------------------------------------------------------------------
# The dates, close prices and Business (trading) day counter lists
# -------------------------------------------------------------------------- 


# ----------------------------------------------------------------------------
#   Create two series
# ----------------------------------------------------------------------------

# Series with prices
prc_ser = pd.Series(data=prices, index=dates)

# Series with trading day
bday_ser = pd.Series(data=bday, index=dates)

# -------------------------------------------------------------------------
# Create a dataframe
# -------------------------------------------------------------------------
# Using the series we created above...
# Data Frame with close and Bday columns
df = pd.DataFrame({'Close': prc_ser, 'Bday': bday_ser})
print(df)
# Output:
# Close Bday
# 2020-01-02 7.16 1
# 2020-01-03 7.19 2
# 2020-01-06 7.00 3
# 2020-01-07 7.10 4
# 2020-01-08 6.86 5

# --------------------------------------------------------------------------
# Accessing the indexes in a dataframe
# --------------------------------------------------------------------------
# The attribute `columns` returns the column index
print(df.columns)
# Output:
# Index(['Close', 'Bday'], dtype='object')
print(type(df.columns))
# Output: <class 'pandas.core.indexes.base.Index'>
# 2020-01-09 6.95 6
# 2020-01-10 7.00 7
# 2020-01-13 7.02 8
# 2020-01-14 7.11 9
# 2020-01-15 7.04 10

col0 = df['Close']
print(col0)
# Output:
# 2020-01-02 7.16
# 2020-01-03 7.19
# 2020-01-06 7.00
# 2020-01-07 7.10
# 2020-01-08 6.86
# 2020-01-09 6.95
# 2020-01-10 7.00
# 2020-01-13 7.02
# 2020-01-14 7.11
# 2020-01-15 7.04
# Name: Close, dtype: float64
print(type(col0))
# Output:
# <class 'pandas.core.series.Series'>

# ----------------------------------------------------------------------------
# Modifying columns and indexes
# ----------------------------------------------------------------------------
# Modify the columns and indexes
df.columns = ['A', 'B']
df.index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(df)
# Then revert back
df.columns = ['Close', 'Bday']
df.index = [
 '2020-01-02', '2020-01-03', '2020-01-06', '2020-01-07', '2020-01-08',
 '2020-01-09', '2020-01-10', '2020-01-13', '2020-01-14', '2020-01-15',
 ]
print(df)

# -------------------------------------------------------------------------
# Sorting
# -------------------------------------------------------------------------
# Create a series with an unsorted index
new_ser = pd.Series(data=[1,3,2], index=['a', 'c', 'b'])
# This will return 'False'
print(new_ser.is_monotonic_increasing)
