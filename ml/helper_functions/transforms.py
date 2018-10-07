from numpy import log1p


def log_transform(df, skew_list):
    '''Applies a log transformation to a list of variables'''
    for col in skew_list:
        df['{}Log'.format(col)] = log1p(df[col])

    return df
