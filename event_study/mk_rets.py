""" mk_rets.py

Utilities to calculate stock and market returns
"""
import pandas as pd

import event_study.config as cfg

# Function to read prices and calculate returns
def mk_ret_df(tic):
    """ Calculates return variables for the ticker `tic`

    Parameters
    ----------
    tic : str
        Ticker

    Returns
    -------
    dataframe
        This data frame has the following structure:
        index: DatetimeIndex
        columns:
            ret: float
                Daily stock returns for this ticker `tic`
            mkt: float
                Daily market returns

    Notes
    -----
    This function perform the following operations:
    1. Get the location of the CSV file with the price information for `tic`
    2. Read the CSV file into a data frame
    3. Calculate stock returns returns
    4. Join market returns

    """

if __name__ == "__main__":
    tic = 'TSLA'
    df = mk_ret_df(tic)
    print(df)
    df.info()