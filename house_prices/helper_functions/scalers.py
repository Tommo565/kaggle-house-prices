from sklearn.preprocessing import MinMaxScaler


def min_max_scaler(df, scale_list):
    '''
    Takes a dataframe and a list of (numeric) variables as an input.
    Scales the list of numeric variables, and returns a new dataframe with the
    scaled variables appended.
    '''

    scaler = MinMaxScaler()
    for col in scale_list:
        col_array = df[col].as_matrix()
        arr_scaled = scaler.fit_transform(col_array.reshape(-1, 1))
        df[col] = arr_scaled

    return df
