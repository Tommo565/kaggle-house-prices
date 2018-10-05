import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def explore_feature(df, feature, target):
    '''
    Takes a dataframe, feature and a target.
    Gets basic statistics & ranks for a (numeric or categorical) variable.
    PLots a seaborn StripPlot of the variables.
    Returns a dataframe of the results.
    '''

    # Stats Table
    tb_mean = df[[feature, target]].groupby(feature).mean()
    tb_med = df[[feature, target]].groupby(feature).median()
    tb_min = df[[feature, target]].groupby(feature).min()
    tb_max = df[[feature, target]].groupby(feature).max()
    tb_std = df[[feature, target]].groupby(feature).std()
    tb_skew = df[[feature, target]].groupby(feature).skew()
    tb_cnt = df[[feature, target]].groupby(feature).count()

    tb = pd.concat(
        [tb_mean, tb_med, tb_min, tb_max, tb_std, tb_skew, tb_cnt],
        axis=1
    )
    tb.reset_index(inplace=True)
    tb.columns = [
        feature, 'mean', 'median', 'min', 'max', 'std', 'skew', 'cnt'
    ]
    tb = tb.round(2)

    cols = tb.columns.tolist()
    cols.remove(target)

    for col in cols:
        tb['{}_rank'.format(col)] = tb[col].rank()

    plt.figure(figsize=(24, 12))
    g = sns.stripplot(
        x=feature,
        y=target,
        data=df,
        size=3,
        alpha=1,
        palette='deep',
        jitter=True
    )
    plt.title(feature)

    return tb
