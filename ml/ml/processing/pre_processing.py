import pandas as pd


def pre_processing(df, none_list, na_list):
    '''
    Pre-processes the data by removing missing values
    '''

    for var in none_list:
        df[var].fillna('None', inplace=True)

    for var in na_list:
        df[var].fillna(0, inplace=True)

    return df
