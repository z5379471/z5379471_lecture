# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# def read_prc_csv(tic):
    """ This function creates a data frame with the contents of a CSV file
    containing stock price information for a given ticker.

    Parameters
    ----------
    tic : str
        String with the ticker
    Returns
    -------
    df
        A Pandas data frame containing the stock price information from the CSV
        containing the stock prices for the ticker `tic`.
        This data frame must meet the following criteria:

        - df.index: `DatetimeIndex` with dates, matching the dates contained in
          the CSV file. The labels in the index must be `datetime` objects.
        - df.columns: each column label will be a column in the CSV file,
          with the exception of 'Date'. Column names will be formatted
          according to the `standardise_colnames` function included in the
          `project2.config.py` module.
    Examples
    --------
    IMPORTANT: The examples below are for illustration purposes. Your ticker/sample
    period may be different.
        >> tic = 'AAPL'
        >> tic_df = read_prc_csv(tic)
        >> tic_df.info()
        DatetimeIndex: 252 entries, 2010-01-04 to 2010-12-31
        Data columns (total 6 columns):
         #   Column     Non-Null Count  Dtype
        ---  ------     --------------  -----
         0   open       252 non-null    float64
         1   high       252 non-null    float64
         2   low        252 non-null    float64
         3   close      252 non-null    float64
         4   adj_close  252 non-null    float64
         5   volume     252 non-null    int64
        dtypes: float64(5), int64(1)
    Hints
    -----
    - Remember that the ticker `tic` in `<tic>`_prc.csv is in lower case.
    - Make sure you use the `standardise_colnames` function in the `config.py`
      module
    """
    # <COMPLETE THIS PART>
    # filename: str = '%s_prc.csv' % tic.lower()
    # path = os.path.join(cfg.DATADIR, filename)
    # data = pd.read_csv(path, parse_dates=['Date'], index_col=['Date'])
    # data = cfg.standardise_colnames(data)
    # return data
prc.sort_index(inplace=True)

# compute returns

rets = prc.loc[꞉ 'Close'].pct_change()

print(rets)
