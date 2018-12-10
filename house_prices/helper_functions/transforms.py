import pandas as pd
from numpy import log1p
from scipy.stats import skew
from scipy.special import boxcox1p


def unskew(df, num_exclude_vars):
    '''
    Checks for skew and performs a Box-Cox transformation to
    highly skewed variables
    '''
    num_vars = df.dtypes[df.dtypes != "object"].index.tolist()
    for exclusion in num_exclude_vars:
        if exclusion in num_vars:
            num_vars.remove(exclusion)

    skew_vars = (
        df[num_vars]
        .apply(lambda x: skew(x.dropna()))
        .sort_values(ascending=False)
    )
    skewness = pd.DataFrame({'Skew': skew_vars})
    skewness = skewness[abs(skewness) > 0.75]

    skewed_cols = skewness.index.tolist()
    lam = 0.15

    for col in skewed_cols:
        df[col] = boxcox1p(df[col], lam)

    return df


def log_transform(df, log_trf_list):
    '''Applies a log transformation to a list of variables'''
    for col in log_trf_list:
        df[col] = log1p(df[col])

    return df


def poly_transform(df, poly_trf_list):
    '''Applies 3 degrees of poly transforms to a list of variables'''
    for col in poly_trf_list:
        df['{}_2'.format(col)] = df[col]**(2)
        df['{}_3'.format(col)] = df[col]**(3)
        df['{}_4'.format(col)] = df[col]**(4)

    return df
