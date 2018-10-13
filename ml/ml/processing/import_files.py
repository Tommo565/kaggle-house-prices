import pandas as pd


def import_files(train_in, test_in):
    '''Imports the train and test sets'''

    df_train = pd.read_csv(train_in)
    df_train['Train'] = 1

    df_test = pd.read_csv(test_in)
    df_test['Test'] = 1

    return df_train, df_test
