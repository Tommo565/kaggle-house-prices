import pandas as pd


def one_hot_encoder(df, one_hot_list):
    '''
    Takes a dataframe and a list of (categorical) variables as an input.
    One-hot encodes a list of categorical variables, and returns a new
    dataframe
    '''

    for col in one_hot_list:

        df_1h = pd.get_dummies(df[col])
        df_1h.columns = ['{}_{}'.format(col, x) for x in df_1h.columns]
        df = pd.concat([df, df_1h], axis=1)

    return df


# Write a Label encoder
