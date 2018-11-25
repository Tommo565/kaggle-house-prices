from numpy import log1p


def log_transform(df, log_trf_list):
    '''Applies a log transformation to a list of variables'''
    for col in log_trf_list:
        df[col] = log1p(df[col])

    return df
