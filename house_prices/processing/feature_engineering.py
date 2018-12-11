import warnings
import pandas as pd
import numpy as np
from helper_functions import (
    one_hot_encoder, min_max_scaler, unskew, log_transform, poly_transform,
    build_ordinal, get_ordinal
)
warnings.filterwarnings('ignore')


def feature_engineering(
    df, target, quality_vars, quality_codes, med_vars, get_ordinal,
    ordinal_vars, num_exclude_vars, one_hot_vars,
    train_model_out, test_model_out, all_model_out
):
    '''
    Wrapper function for feature engineering
    '''

    # Manual replacement (hack)
    df['MSSubClass'].replace({150, '180'}, inplace=True)

    # Replace qualily codes with Ordinal values
    for item in quality_vars:
        df[item].replace(quality_codes, inplace=True)

    # One hot encoding
    df = one_hot_encoder(df, one_hot_vars)

    # Build the ordinal ranks from the train data
    build_ordinal(df[(df['Train'] == 1)], ordinal_vars, target)

    # Apply the ordinal ranks to the train / test data
    for var in get_ordinal():
        for key, value in var.items():
            df[key] = df[key].replace(value)

    # Handle skew
    df = unskew(df, num_exclude_vars)

    # Scale
    # df = min_max_scaler(df, num_exclude_vars)

    # Log Transform Target
    df[target] = np.log1p(df[target])

    # Export
    df[(df['Train'] == 1)].to_csv(train_model_out, index=False)
    print('Train Dataset created')

    df[(df['Test'] == 1)].to_csv(test_model_out, index=False)
    print('Test Dataset created')

    df.to_csv(all_model_out, index=False)
    print('Train & Test Dataset Created')

    return df
