import json
import pandas as pd


def to_ordinal_med(df, feature, target):
    '''
    Converts a categorical variable to an ordinal variable based upon the
    median values
    '''

    tb_med = df[[feature, target]].groupby(feature).median().reset_index()
    tb_med['{}_rank'.format(feature)] = tb_med[target].rank().astype('int')
    tb_med = (
        tb_med.sort_values('{}_rank'.format(feature))
        .set_index(feature)
        .drop([target], axis=1)
    )
    out_dict = tb_med.to_dict()
    values = out_dict['{}_rank'.format(feature)]

    with open('./parameters/{}_rank.json'.format(feature), 'w') as f:
        json.dump(values, f, indent=4)


def get_ordinal_values(feature):

    with open('./parameters/{}_rank.json'.format(feature)) as f:
        values = json.load(f)

    return values
