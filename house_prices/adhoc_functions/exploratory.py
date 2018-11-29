import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

''' Cat matrix - compare categorical variables '''
''' Explore numeric feature '''


def correlation_heatmap(df, method='pearson', drop_vars=[], keep_vars=[]):
    '''
    Takes a dataframe and a list of variable names.
    Produces a heatmap, excluding the variable names listed in the
    dropvars list.
    Returns a seaborn heatmap.

    Improve this docstring
    '''

    if drop_vars != []:
        df_corr = df.corr(method=method).round(1).drop(drop_vars, axis=1)

    elif keep_vars != []:
        df_corr = df[keep_vars].corr(method=method).round(1)

    else:
        df_corr = df.corr(method=method).round(1)

    plt.figure(figsize=(30, 15))
    ax = sns.heatmap(
        df_corr,
        cmap='coolwarm',
        linewidths=1,
        annot=True,
        annot_kws={
            'size': 12
        }
    )

    return df_corr


def explore_feature(df, feature, target, font_scale=1, palette='bright'):
    '''
    Takes a dataframe, feature and a target.
    Gets basic statistics & ranks for a (numeric or categorical) variable.
    PLots a seaborn StripPlot of the variables.
    Returns a dataframe of the results.
    '''

    sns.set(font_scale=font_scale)

    tb_vars = [feature, target]

    # Stats Table
    tb_mean = df[tb_vars].groupby(feature).mean()
    tb_med = df[tb_vars].groupby(feature).median()
    tb_min = df[tb_vars].groupby(feature).min()
    tb_max = df[tb_vars].groupby(feature).max()
    tb_std = df[tb_vars].groupby(feature).std()
    tb_skew = df[tb_vars].groupby(feature).skew()
    tb_cnt = df[tb_vars].groupby(feature).count()

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
        palette=palette,
        ax=violin_ax
    )

    strip_chart, strip_ax = plt.subplots(figsize=(32, 16))
    sns.stripplot(
        x=feature,
        y=target,
        data=df,
        size=3,
        alpha=1,
        palette=palette,
        jitter=True,
        ax=strip_ax
    )

    return tb


def explore_feature_hue(
        df, feature1, target, feature2, font_scale=1, palette='Reds'
):
    '''
    Takes a dataframe, feature and a target.
    Gets basic statistics & ranks for a (numeric or categorical) variable.
    PLots a seaborn StripPlot of the variables.
    Returns a dataframe of the results.
    '''

    sns.set(font_scale=font_scale)

    strip_chart, strip_ax = plt.subplots(figsize=(32, 16))
    sns.stripplot(
        x=feature1,
        y=target,
        hue=feature2,
        data=df,
        size=3,
        alpha=1,
        palette=palette,
        jitter=True,
        ax=strip_ax
    )
