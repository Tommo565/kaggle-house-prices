import json
import pandas as pd


def build_ordinal(df, ordinal_vars, target):
    '''
    Converts a categorical variable to an ordinal variable based upon the
    median values
    '''
    ord_output = []

    for var in ordinal_vars:
        tb_med = df[[var, target]].groupby(var).median().reset_index()
        tb_med['{}_rank'.format(var)] = tb_med[target].rank().astype('int')
        tb_med = (
            tb_med.sort_values('{}_rank'.format(var))
            .set_index(var)
            .drop([target], axis=1)
            .rename(columns={
                '{}_rank'.format(var): var})
        )

        out_dict = tb_med.to_dict()
        values = out_dict[var]
        ord_output.append(out_dict)

    with open('./parameters/ordinal_ranks.json', 'w') as f:
        json.dump(ord_output, f, indent=4)


def get_ordinal():

    with open('./parameters/ordinal_ranks.json') as f:
        ordinal_ranks = json.load(f)

    return ordinal_ranks
