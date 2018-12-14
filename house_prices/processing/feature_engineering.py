import warnings
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from helper_functions import (
    one_hot_encoder, min_max_scaler, log_transform, poly_transform,
    build_ordinal, get_ordinal, label_encoder
)
warnings.filterwarnings('ignore')


def feature_engineering(
    df, target, quality_vars, quality_codes, one_hot_vars, ordinal_vars,
    label_vars, num_vars,
    train_model_out, test_model_out, all_model_out
):
    '''
    Wrapper function for feature engineering
    '''

    #  Hack
    df['MSSubClass'].replace({'150', '180'}, inplace=True)

    # 2. Create Ordinal Variables

    # Replace qualily codes with Ordinal values
    for item in quality_vars:
        df[item].replace(quality_codes, inplace=True)

    # Build the ordinal ranks from the train data
    build_ordinal(df[(df['Train'] == 1)], ordinal_vars, target)

    # Apply the ordinal ranks to the train / test data
    for var in get_ordinal():
        for key, value in var.items():
            name = 'Ord_{}'.format(key)
            df[name] = df[key].replace(value)
            num_vars.append(name)

    #  Hack
    num_vars.remove('Ord_MSSubClass')

    # 3. New Variables

    # Total Area
    df['TotalArea'] = (
        df['TotalBsmtSF'] + df['GrLivArea'] + df['1stFlrSF'] + df['2ndFlrSF']
    )
    num_vars.append('TotalArea')

    # Core Area
    df['CoreArea'] = df['TotalBsmtSF'] + df['GrLivArea']
    num_vars.append('CoreArea')

    # 4. Transformations
    df = one_hot_encoder(df, one_hot_vars)
    df = label_encoder(df, label_vars)
    df, num_vars = log_transform(df, num_vars)
    df = min_max_scaler(df, num_vars)

    df[target] = np.log1p(df[target])

    # 6. Sort columns
    df = df.reindex(sorted(df.columns), axis=1)

    # 7. Export
    df[(df['Train'] == 1)].to_csv(train_model_out, index=False)
    print('Train Dataset created')

    df[(df['Test'] == 1)].to_csv(test_model_out, index=False)
    print('Test Dataset created')

    df.to_csv(all_model_out, index=False)
    print('Train & Test Dataset Created')

    return df
