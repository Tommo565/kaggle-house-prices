import pandas as pd
from sklearn.preprocessing import LabelEncoder


def one_hot_encoder(df, one_hot_vars):
    '''
    Takes a dataframe and a list of (categorical) variables as an input.
    One-hot encodes a list of categorical variables, and returns a new
    dataframe
    '''

    for col in one_hot_vars:
        df_1h = pd.get_dummies(df[col])
        df_1h.columns = ['{}_{}'.format(col, x) for x in df_1h.columns]
        df = pd.concat([df, df_1h], axis=1)

    return df


def label_encoder(df, label_vars):
    '''
    Takes a dataframe and a list of (categorical) variables as an input.
    Label encodes a list of categorical variables, and returns a new
    dataframe
    '''

    for col in label_vars:
        Enc = LabelEncoder()
        Enc.fit(df[col])
        df[col] = Enc.transform(df[col])

    return df
