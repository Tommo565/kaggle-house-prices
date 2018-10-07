import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

''' Cat matrix - compare categorical variables '''
''' Explore numeric feature '''


def correlation_heatmap(df, drop_vars):
    '''
    Takes a dataframe and a list of variable names.
    Produces a heatmap, excluding the variable names listed in the
    dropvars list.
    Returns a seaborn heatmap.
    '''

    df_corr = df.corr().round(1).drop(drop_vars, axis=1)
    plt.figure(figsize=(30, 15))
    ax = sns.heatmap(
        df_corr,
        cmap='coolwarm',
        linewidths=1,
        annot=True,
        annot_kws={
            'size': 15
        }
    )


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
    cols.remove(feature)

    for col in cols:
        tb['{}_rank'.format(col)] = tb[col].rank(ascending=False)

    violin_chart, violin_ax = plt.subplots(figsize=(32, 16))
    sns.violinplot(
        x=feature,
        y=target,
        data=df,
        size=3,
        alpha=1,
        palette='deep',
        ax=violin_ax
    )

    strip_chart, strip_ax = plt.subplots(figsize=(32, 16))
    sns.stripplot(
        x=feature,
        y=target,
        data=df,
        size=3,
        alpha=1,
        palette='deep',
        jitter=True,
        ax=strip_ax
    )

    return tb


def explore_feature_hue(df, feature, target, hue):
    '''
    Takes a dataframe, feature and a target.
    Gets basic statistics & ranks for a (numeric or categorical) variable.
    PLots a seaborn StripPlot of the variables.
    Returns a dataframe of the results.
    '''

    strip_chart, strip_ax = plt.subplots(figsize=(32, 16))
    sns.stripplot(
        x=feature,
        y=target,
        hue=hue,
        data=df,
        size=3,
        alpha=1,
        palette='Reds',
        jitter=True,
        ax=strip_ax
    )
