import os

import pandas as pd

from project2 import config as cfg

def read_prc_csv(tic):
    new_name = '%s_prc.csv' % tic.lower()
    pth = os.path.join(cfg.DATADIR, new_name)
    data = pd.read_csv(pth, parse_dates=['Date'], index_col='Date')
    data = cfg.standardise_colnames(data)
    return data



def _test_read_prc_csv():
    """ Test function for `read_prc_csv`
    """
    tic = 'AAPL'
    df = read_prc_csv(tic)
    _test_print(df)

tic = 'AAPL'
tic_df= read_prc_csv('AAPL')
tic_df.info()


