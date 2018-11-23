import warnings
import pandas as pd
from helper_functions import one_hot_encoder, min_max_scaler, log_transform
from .transformation_functions import *
warnings.filterwarnings('ignore')


def feature_engineering_linear(
    df, data, target, quality_vars, quality_codes, simple_codes, med_list,
    explore_out_linear, train_model_out_linear, test_model_out_linear,
    features, scale_list, one_hot_list, log_trf_list
):
    '''Performs the feature engineering on the dataset for linear modelling'''

    # Convert numeric to categorical
    df['MSSubClass'] = df['MSSubClass'].astype(str)

    # Code the quality variables
    for item in quality_vars:
        df[item].replace(quality_codes, inplace=True)

    # Fills na with median values
    for item in med_list:
        df[item].fillna(df[item].median(), inplace=True)

    # Create new variables
    df['HasPorch'] = df.apply(has_porch, axis=1)
    df['IsRemodelled'] = df.apply(is_remodelled, axis=1)
    df['PropertyAge'] = df.apply(property_age, axis=1)
    df['FullBath'] = df.apply(full_bath, axis=1)
    df['HalfBath'] = df.apply(half_bath, axis=1)
    df['TotalBath'] = df['FullBath'] + (df['HalfBath'] * 0.5)
    df['HasPool'] = df.apply(has_pool, axis=1)
    df['HasDeck'] = df.apply(has_deck, axis=1)
    df['YrSold'] = df['YrSold'] - 2005
    df['IsNew'] = df.apply(is_new, axis=1)
    df['IsPartial'] = df.apply(is_partial, axis=1)

    # Combination Variables
    df['OverallGrade'] = df['OverallQual'] * df['OverallCond']
    df['ExterGrade'] = df["ExterQual"] * df["ExterCond"]
    df['TotalArea'] = (
        df['TotalBsmtSF'] + df['1stFlrSF'] + df['2ndFlrSF'] + df['GrLivArea']
    )
    df['CoreArea'] = df['GrLivArea'] + df['TotalBsmtSF']

    # Simple Variables
    df['SimpleOverallQual'] = df['OverallQual'].replace(simple_codes)
    df['SimpleOverallCond'] = df['OverallCond'].replace(simple_codes)

    if data == 'Train':

        # Binning the target into bands for exploration
        df['SalePriceBand'] = pd.qcut(
            df['SalePrice'],
            q=10,
            labels=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        )

        # Export a dataset for exploration
        df.to_csv(explore_out_linear, index=False)
        print('Exploration dataset created: {}'.format(explore_out_linear))

        # Remove outliers
        df = df[((df['TotalArea'] <= 10000))]

        # Limit to appropriate features
        df_f = df[features]
        df_t = df[target]
        df = pd.concat([df_f, df_t], axis=1)

    if data == 'Test':
        df = df[features]

    # Scaling
    df = min_max_scaler(df, scale_list)

    # One-hot encoding
    df = one_hot_encoder(df, one_hot_list)

    # Log Transforms
    log_transform(df, log_trf_list)

    if data == 'Train':
        log_transform(df, [target])
        df.to_csv(train_model_out_linear, index=False)
        print('Train model dataset created: {}'.format(train_model_out_linear))

    if data == 'Test':
        df.to_csv(test_model_out_linear, index=False)
        print('Test model dataset created: {}'.format(test_model_out_linear))

    return df
