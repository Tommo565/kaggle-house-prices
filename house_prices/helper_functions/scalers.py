from sklearn.preprocessing import MinMaxScaler


def min_max_scaler(df, num_exclude_vars):
    '''
    Takes a dataframe and a list of (numeric) variables as an input.
    Scales the list of numeric variables, and returns a new dataframe with the
    scaled variables appended.
    '''

    scaler = MinMaxScaler()
    num_vars = df.dtypes[df.dtypes != "object"].index.tolist()
    for exclusion in num_exclude_vars:
        if exclusion in num_vars:
            num_vars.remove(exclusion)

    for col in num_vars:
        col_array = df[col].as_matrix()
        arr_scaled = scaler.fit_transform(col_array.reshape(-1, 1))
        df[col] = arr_scaled

    return df
