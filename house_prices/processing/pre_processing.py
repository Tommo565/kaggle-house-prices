import pandas as pd


def pre_processing(
        df, drop_vars, none_vars, na_vars, mode_vars, med_vars, to_string_vars
):
    '''
    Pre-processes the data by removing missing values
    '''

    df.drop(drop_vars, axis=1, inplace=True)

    # Fill missing values with 'None'
    for var in none_vars:
        df[var].fillna('None', inplace=True)

    # Fill missing values with 0
    for var in na_vars:
        df[var].fillna(0, inplace=True)

    # Fill missing values with the mode
    for var in mode_vars:
        mode_var = df[var].mode()[0]
        df[var] = df[var].fillna(mode_var)

    # Convert numeric to string
    for var in to_string_vars:
        df[var] = df[var].astype(str)

    # Fill missing values with the median or the median for a particular
    # group
    for item in med_vars:
        if item['group'] is not None:
            var = item['var']
            group = item['group']

            df[var] = df.groupby(group)[var].transform(
                lambda x: x.fillna(x.median())
            )

        else:
            median_var = df[var].median()
            df[var].fillna(median_var)



    return df
