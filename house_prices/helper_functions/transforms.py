import pandas as pd
from numpy import log1p
from scipy.stats import skew
from scipy.special import boxcox1p


def log_transform(df, num_vars):
    '''Applies a log transformation to a list of variables'''
    num_vars_out = []

    for col in num_vars:

        df['Log_{}'.format(col)] = log1p(df[col])
        df['Raw_{}'.format(col)] = df[col]
        df = df.drop([col], axis=1)
        num_vars_out.append('Log_{}'.format(col))
        num_vars_out.append('Raw_{}'.format(col))

    return df, num_vars_out


def poly_transform(df, poly_trf_list):
    '''Applies 3 degrees of poly transforms to a list of variables'''
    for col in poly_trf_list:
        df['ply_{}_2'.format(col)] = df[col]**(2)
        df['ply_{}_3'.format(col)] = df[col]**(3)
        df['ply_{}_4'.format(col)] = df[col]**(4)

    return df
